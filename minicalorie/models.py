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
    authors = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    year = models.CharField(max_length=4, blank=True, null=True)
    journal = models.CharField(max_length=135, blank=True, null=True)
    vol_city = models.CharField(max_length=16, blank=True, null=True)
    issue_state = models.CharField(max_length=5, blank=True, null=True)
    start_page = models.CharField(max_length=5, blank=True, null=True)
    end_page = models.CharField(max_length=5, blank=True, null=True)


class Footnote(models.Model):
    """Contains additional information about the food item, household weight, and nutrient value.

    Source: FOOTNOTE.txt in USDA SR28
    """
    ndb_no = models.CharField(max_length=5, blank=False, null=False)
    footnt_no = models.CharField(max_length=4, blank=False, null=False)
    footnt_typ = models.CharField(max_length=1, blank=False, null=False)
    nutr_no = models.CharField(max_length=3, blank=True, null=True)
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
    comname = models.CharField(max_length=100, blank=True, null=True)
    manufacname = models.CharField(max_length=65, blank=True, null=True)
    survey = models.CharField(max_length=1, blank=True, null=True)
    ref_desc = models.CharField(max_length=135, blank=True, null=True)
    refuse = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    sciname = models.CharField(max_length=65, blank=True, null=True)
    n_factor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    pro_factor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    fat_factor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cho_factor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('ndb_no', 'fdgrp_cd',)


class NutrDef(models.Model):
    """Provides the 3-digit nutrient code, unit of measure, INFOODS tagname, and description.

    Source: NUTR_DEF.txt in USDA SR28
    """
    nutr_no = models.CharField(max_length=3, blank=False, null=False, primary_key=True)
    units = models.CharField(max_length=7, blank=False, null=False)
    tagname = models.CharField(max_length=20, blank=True, null=True)
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
    std_error = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    src_cd = models.CharField(max_length=2, blank=False, null=False)
    deriv_cd = models.CharField(max_length=4, blank=True, null=True)
    ref_ndb_no = models.CharField(max_length=5, blank=True, null=True)
    add_nutr_mark = models.CharField(max_length=1, blank=True, null=True)
    num_studies = models.IntegerField(blank=True, null=True)
    min = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    max = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    df = models.IntegerField(blank=True, null=True)
    low_eb = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    up_eb = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    stat_cmt = models.CharField(max_length=10, blank=True, null=True)
    addmod_date = models.CharField(max_length=10, blank=True, null=True)
    cc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        unique_together = ('ndb_no', 'nutr_no', )


class Weight(models.Model):
    """Weight in grams of a number of common measures for each food item

    Source: WEIGHT.txt in USDA SR28
    """
    ndb_no = models.ForeignKey(FoodDes, to_field='ndb_no', blank=False, null=False)
    seq = models.CharField(max_length=2, blank=False, null=False)
    amount = models.DecimalField(max_digits=6, decimal_places=3, blank=False, null=False)
    msre_desc = models.CharField(max_length=84, blank=False, null=False)
    gm_wgt = models.DecimalField(max_digits=7, decimal_places=1, blank=False, null=False)
    num_data_pts = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    std_dev = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)

    class Meta:
        unique_together = ('ndb_no', 'seq', )


class Langual(models.Model):
    """Factors from the LanguaL Thesaurus used to code a particular food

    Source: LANGUAL.txt in USDA SR28
    """
    ndb_no = models.ForeignKey(FoodDes, to_field='ndb_no', blank=False, null=False)
    factor_code = models.ForeignKey(Langdesc, to_field='factor_code', blank=False, null=False)

    class Meta:
        unique_together = ('ndb_no', 'factor_code', )


class Datsrcln(models.Model):
    """Link the Nutrient Data table with the Sources of Data table

    Source: DATSRCLN.txt in USDA SR28
    """
    ndb_no = models.ForeignKey(FoodDes, to_field='ndb_no', blank=False, null=False)
    nutr_no = models.ForeignKey(NutrDef, to_field='nutr_no', blank=False, null=False)
    datasrc_id = models.ForeignKey(DataSrc, to_field='datasrc_id', blank=False, null=False)

    class Meta:
        unique_together = ('ndb_no', 'nutr_no', 'datasrc_id', )
