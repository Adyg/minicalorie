from django.db import models


class SrcCd(models.Model):
    """Codes indicating the type of data in the Nutrient Data table.

    Source: SRC_CD.txt in USDA SR28
    """
    src_cd = models.CharField(max_length=2, blank=False, null=False, primary_key=True)
    srccd_desc = models.CharField(max_length=60, blank=False, null=False)


class DerivCd(models.Model):
    """Provides information on how the nutrient values were determined.

    Source: DERIV_CD.txt in USDA SR28
    """
    deriv_cd = models.CharField(max_length=4, blank=False, null=False, primary_key=True)
    deriv_desc = models.CharField(max_length=120, blank=False, null=False)


class DataSrc(models.Model):
    """Provides a citation to the DataSrc_ID in the Sources of Data Link table.

    Source: DATA_SRC.txt in USDA SR28
    """
    datasrc_id = models.CharField(max_length=6, blank=False, null=False, primary_key=True)
    authors = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=False, null=False)
    year = models.CharField(max_length=4)
    journal = models.CharField(max_length=135)
    vol_city = models.CharField(max_length=16)
    issue_state = models.CharField(max_length=5)
    start_page = models.CharField(max_length=5)
    end_page = models.CharField(max_length=5)


class Footnote(models.Model):
    """Contains additional information about the food item, household weight, and nutrient value.

    Source: FOOTNOTE.txt in USDA SR28
    """
    ndb_no = models.CharField(max_length=5, blank=False, null=False)
    footnt_no = models.CharField(max_length=4, blank=False, null=False)
    footnt_typ = models.CharField(max_length=1, blank=False, null=False)
    nutr_no = models.CharField(max_length=3)
    footnt_txt = models.CharField(max_length=200, blank=False, null=False)


class Langdesc(models.Model):
    """Contains the descriptions for only those factors used in coding the selected food items codes.

    Source: LANGDESC.txt in USDA SR28
    """
    factor_code = models.CharField(max_length=5, blank=False, null=False, primary_key=True)
    description = models.CharField(max_length=200, blank=False, null=False)


class FdGroup(models.Model):
    """Contains a list of food groups used in SR28 and their descriptions.

    Source: FD_GROUP.txt in USDA SR28
    """
    fdgrp_cd = models.CharField(max_length=4, blank=False, null=False, primary_key=True)
    fdgrp_desc = models.CharField(max_length=60, blank=False, null=False)


class FoodDes(models.Model):
    """Descriptions and food group designators for all food items.

    Contains long and short descriptions and food group designators for all food items, along with common
    names, manufacturer name, scientific name, percentage and description of refuse, and
    factors used for calculating protein and kilocalories, if applicable. Items used in the
    FNDDS are also identified by value of "Y" in the Survey field.

    Source: FOOD_DES.txt in USDA SR28
    """
    ndb_no = models.CharField(max_length=5, blank=False, null=False, primary_key=True)
    fdgrp_cd = models.ForeignKey(FdGroup, to_field='fdgrp_cd')
    long_desc = models.CharField(max_length=200, blank=False, null=False)
    shrt_desc = models.CharField(max_length=60, blank=False, null=False)
    comname = models.CharField(max_length=100)
    manufacname = models.CharField(max_length=65)
    survey = models.CharField(max_length=1)
    ref_desc = models.CharField(max_length=135)
    refuse = models.IntegerField()
    sciname = models.CharField(max_length=65)
    n_factor = models.DecimalField(max_digits=4, decimal_places=2)
    pro_factor = models.DecimalField(max_digits=4, decimal_places=2)
    fat_factor = models.DecimalField(max_digits=4, decimal_places=2)
    cho_factor = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        unique_together = ('ndb_no', 'fdgrp_cd',)


class NutrDef(models.Model):
    """Provides the 3-digit nutrient code, unit of measure, INFOODS tagname, and description.

    Source: NUTR_DEF.txt in USDA SR28
    """
    nutr_no = models.CharField(max_length=3, blank=False, null=False, primary_key=True)
    units = models.CharField(max_length=7, blank=False, null=False)
    tagname = models.CharField(max_length=20)
    nutrdesc = models.CharField(max_length=60, blank=False, null=False)
    num_dec = models.CharField(max_length=1, blank=False, null=False)
    sr_order = models.IntegerField(blank=False, null=False)


class NutData(models.Model):
    """Nutrient values and information about the values.

    Contains the nutrient values and information about the values, including expanded statistical information.

    Source: NUT_DATA.txt in USDA SR28
    """
    ndb_no = models.ForeignKey(FoodDes, to_field='ndb_no', blank=False, null=False)
    nutr_no = models.ForeignKey(NutrDef, to_field='nutr_no', blank=False, null=False)
    nutr_val = models.DecimalField(max_digits=10, decimal_places=3, blank=False, null=False)
    num_data_pts = models.DecimalField(max_digits=5, decimal_places=0, blank=False, null=False)
    std_error = models.DecimalField(max_digits=8, decimal_places=3)
    src_cd = models.CharField(max_length=2, blank=False, null=False)
    deriv_cd = models.CharField(max_length=4)
    ref_ndb_no = models.CharField(max_length=5)
    add_nutr_mark = models.CharField(max_length=1)
    num_studies = models.IntegerField()
    min = models.DecimalField(max_digits=10, decimal_places=3)
    max = models.DecimalField(max_digits=10, decimal_places=3)
    df = models.IntegerField()
    low_eb = models.DecimalField(max_digits=10, decimal_places=3)
    up_eb = models.DecimalField(max_digits=10, decimal_places=3)
    stat_cmt = models.CharField(max_length=10)
    addmod_date = models.CharField(max_length=10)
    cc = models.CharField(max_length=1)

    class Meta:
        unique_together = ('ndb_no', 'nutr_no', )


class Weight(models.Model):
    """Weight in grams of a number of common measures for each food item

    Source: WEIGHT.txt in USDA SR28
    """
    ndb_no = models.ForeignKey(FoodDes, to_field='ndb_no', blank=False, null=False)
    seq = models.CharField(max_length=2, blank=False, null=False)
    amount = models.DecimalField(max_digits=6, decimal_places=3, blank=False, null=False)
    msre_desc = models.CharField(max_length=64, blank=False, null=False)
    gm_wgt = models.DecimalField(max_digits=7, decimal_places=1, blank=False, null=False)
    num_data_pts = models.DecimalField(max_digits=4, decimal_places=0)
    std_dev = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=False)

    class Meta:
        unique_together = ('ndb_no', 'seq', )
