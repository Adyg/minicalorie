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
