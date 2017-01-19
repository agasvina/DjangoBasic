from __future__ import unicode_literals

from django.db import models


class Ablation(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.TextField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.TextField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    stdate = models.TextField(db_column='STDATE', blank=True, null=True)  # Field name made lowercase.
    method = models.TextField(db_column='METHOD', blank=True, null=True)  # Field name made lowercase.
    organ = models.TextField(db_column='ORGAN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ablation'


class Ablationmethodlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AblationMethodLUT'


class Ablationorganlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AblationOrganLUT'


class Chemolocationlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChemoLocationLUT'


class Chemomateriallut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    chemo = models.TextField(db_column='Chemo', blank=True, null=True)  # Field name made lowercase.
    current = models.IntegerField(db_column='Current', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChemoMaterialLUT'


class Chemomethodlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChemoMethodLUT'


class Chemotherapy(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    material = models.TextField(db_column='MATERIAL', blank=True, null=True)  # Field name made lowercase.
    stdate = models.TextField(db_column='STDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enddate = models.TextField(db_column='ENDDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    method = models.IntegerField(db_column='METHOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chemotherapy'


class Civilstatuslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CivilStatusLUT'


class Copyofsitelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CopyOfSiteLUT'


class Fustateofmetslut(models.Model):
    iindex = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUStateOfMetsLUT'


class Fustateofnodeslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUStateOfNodesLUT'


class Fustateofprimarylut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUStateOfPrimaryLUT'


class Fusummarynodeslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUSummaryNodesLUT'


class Fusummaryprimarylut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUSummaryPrimaryLUT'


class Futypelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True, unique=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUTypeLUT'


class Followup(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    fudate = models.TextField(db_column='FUDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    futype = models.ForeignKey('Futypelut', db_column='FUTYPE', to_field='code', blank=True, null=True)
    primstat = models.FloatField(db_column='PRIMSTAT', blank=True, null=True)  # Field name made lowercase.
    nodestat = models.FloatField(db_column='NODESTAT', blank=True, null=True)  # Field name made lowercase.
    metastat = models.FloatField(db_column='METASTAT', blank=True, null=True)  # Field name made lowercase.
    nogpask = models.IntegerField(db_column='NOGPASK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FollowUp'


class Histologylut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    shorttext = models.TextField(db_column='ShortText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistologyLUT'


class Histologyoutcomelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistologyOutcomeLUT'


class Hormone(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    stdate = models.TextField(db_column='STDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enddate = models.TextField(db_column='ENDDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.IntegerField(db_column='MATERIAL', blank=True, null=True)  # Field name made lowercase.
    method = models.IntegerField(db_column='METHOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hormone'


class Hormonemateriallut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HormoneMaterialLUT'


class Hormonemethodlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HormoneMethodLUT'


class Hospitallut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospitalLUT'


class Implantmateriallut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImplantMaterialLUT'


class Implantmethodlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImplantMethodLUT'


class Implants(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.TextField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.TextField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    stdate = models.TextField(db_column='STDATE', blank=True, null=True)  # Field name made lowercase.
    material = models.TextField(db_column='MATERIAL', blank=True, null=True)  # Field name made lowercase.
    method = models.TextField(db_column='METHOD', blank=True, null=True)  # Field name made lowercase.
    timehrs = models.TextField(db_column='TIMEHRS', blank=True, null=True)  # Field name made lowercase.
    mintdose = models.TextField(db_column='MINTDOSE', blank=True, null=True)  # Field name made lowercase.
    targvol = models.TextField(db_column='TARGVOL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Implants'


class Inoutpatientlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InOutPatientLUT'


class Intracav(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.TextField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.TextField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    stdate = models.TextField(db_column='STDATE', blank=True, null=True)  # Field name made lowercase.
    material = models.TextField(db_column='MATERIAL', blank=True, null=True)  # Field name made lowercase.
    method = models.TextField(db_column='METHOD', blank=True, null=True)  # Field name made lowercase.
    timehrs = models.TextField(db_column='TIMEHRS', blank=True, null=True)  # Field name made lowercase.
    totdose = models.TextField(db_column='TOTDOSE', blank=True, null=True)  # Field name made lowercase.
    dose2cm = models.TextField(db_column='DOSE2CM', blank=True, null=True)  # Field name made lowercase.
    dose5cm = models.TextField(db_column='DOSE5CM', blank=True, null=True)  # Field name made lowercase.
    critorg1 = models.TextField(db_column='CRITORG1', blank=True, null=True)  # Field name made lowercase.
    dose1 = models.TextField(db_column='DOSE1', blank=True, null=True)  # Field name made lowercase.
    critorg2 = models.TextField(db_column='CRITORG2', blank=True, null=True)  # Field name made lowercase.
    dose2 = models.TextField(db_column='DOSE2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Intracav'


class Intracavcriticalorgan1Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntracavCriticalOrgan1LUT'


class Intracavcriticalorgan2Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntracavCriticalOrgan2LUT'


class Intracavmateriallut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntracavMaterialLUT'


class Intracavmethodlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntracavMethodLUT'


class M1Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M1LUT'


class M2Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M2LUT'


class Mlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MLUT'


class Mvaluelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MValueLUT'


class Machinelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    energy = models.IntegerField(db_column='Energy', blank=True, null=True)  # Field name made lowercase.
    unit = models.TextField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    factor = models.FloatField(db_column='Factor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MachineLUT'


class Morbidity(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.TextField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.TextField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    mordate = models.TextField(db_column='MORDATE', blank=True, null=True)  # Field name made lowercase.
    morbid = models.TextField(db_column='MORBID', blank=True, null=True)  # Field name made lowercase.
    morsite = models.TextField(db_column='MORSITE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Morbidity'


class Morbiditylut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MorbidityLUT'


class N1Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'N1LUT'


class N2Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'N2LUT'


class Nlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NLUT'


class Nvaluelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NValueLUT'


class Newmets(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    metfndte = models.TextField(db_column='METFNDTE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    metsite = models.TextField(db_column='METSITE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewMets'


class Newnode(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.TextField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.TextField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.TextField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    nodfndte = models.TextField(db_column='NODFNDTE', blank=True, null=True)  # Field name made lowercase.
    nodsite1 = models.TextField(db_column='NODSITE1', blank=True, null=True)  # Field name made lowercase.
    nodsite2 = models.TextField(db_column='NODSITE2', blank=True, null=True)  # Field name made lowercase.
    nodclas1 = models.TextField(db_column='NODCLAS1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewNode'


class Newnodesitelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewNodeSiteLUT'


class Newnodesclasslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewNodesClassLUT'


class Newprimary(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    npdate = models.TextField(db_column='NPDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    npsite = models.TextField(db_column='NPSITE', blank=True, null=True)  # Field name made lowercase.
    nptnm1 = models.TextField(db_column='NPTNM1', blank=True, null=True)  # Field name made lowercase.
    nptnm2 = models.TextField(db_column='NPTNM2', blank=True, null=True)  # Field name made lowercase.
    nptnm3 = models.TextField(db_column='NPTNM3', blank=True, null=True)  # Field name made lowercase.
    nptnm4 = models.TextField(db_column='NPTNM4', blank=True, null=True)  # Field name made lowercase.
    nptnm5 = models.TextField(db_column='NPTNM5', blank=True, null=True)  # Field name made lowercase.
    nptnm6 = models.TextField(db_column='NPTNM6', blank=True, null=True)  # Field name made lowercase.
    nptnm_t = models.TextField(db_column='NPTNM_T', blank=True, null=True)  # Field name made lowercase.
    nptnm_n = models.TextField(db_column='NPTNM_N', blank=True, null=True)  # Field name made lowercase.
    nptnm_m = models.TextField(db_column='NPTNM_M', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewPrimary'


class Newprimarylut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewPrimaryLUT'


class Notreatmentreasonlut(models.Model):
    iindex = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NoTreatmentReasonLUT'


class Nodesiteextendedlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NodeSiteExtendedLUT'


class Nodesitelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NodeSiteLUT'


class Oncconsultantlut(models.Model):
    index = models.TextField(primary_key=True)
    onccons = models.TextField(db_column='ONCCONS', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    surname = models.TextField(db_column='Surname', blank=True, null=True)  # Field name made lowercase.
    initials = models.TextField(db_column='Initials', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='Firstname', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    current = models.IntegerField(db_column='Current', blank=True, null=True)  # Field name made lowercase.
    left = models.TextField(db_column='Left', blank=True, null=True)  # Field name made lowercase.
    speciality = models.TextField(db_column='Speciality', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OncConsultantLUT'


class Oplut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpLUT'


class Performancestatuslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerformanceStatusLUT'


class Placeofbirthlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlaceOfBirthLUT'


class Radicalpalliativelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RadicalPalliativeLUT'


class Radionucmateriallut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RadionucMaterialLUT'


class Radionucmethodlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RadionucMethodLUT'


class Radiotherapy(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    stdate = models.TextField(db_column='STDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enddate = models.TextField(db_column='ENDDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    machine = models.IntegerField(db_column='MACHINE', blank=True, null=True)  # Field name made lowercase.
    tech = models.TextField(db_column='TECH', blank=True, null=True)  # Field name made lowercase.
    extnm = models.IntegerField(db_column='EXTNM', blank=True, null=True)  # Field name made lowercase.
    radpall = models.IntegerField(db_column='RADPALL', blank=True, null=True)  # Field name made lowercase.
    extsite = models.TextField(db_column='EXTSITE', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    xtisdose = models.IntegerField(db_column='XTISDOSE', blank=True, null=True)  # Field name made lowercase.
    critorg = models.TextField(db_column='CRITORG', blank=True, null=True)  # Field name made lowercase.
    critdose = models.TextField(db_column='CRITDOSE', blank=True, null=True)  # Field name made lowercase.
    nofract = models.IntegerField(db_column='NOFRACT', blank=True, null=True)  # Field name made lowercase.
    timedays = models.IntegerField(db_column='TIMEDAYS', blank=True, null=True)  # Field name made lowercase.
    tumdose = models.IntegerField(db_column='TUMDOSE', blank=True, null=True)  # Field name made lowercase.
    maxdose = models.IntegerField(db_column='MAXDOSE', blank=True, null=True)  # Field name made lowercase.
    mindose = models.FloatField(db_column='MINDOSE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Radiotherapy'


class Religionlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReligionLUT'


class Sexlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SexLUT'


class Sidelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SideLUT'


class Sidemainlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SideMainLUT'


class Sitelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SiteLUT'


class Sitewithsidelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SiteWithSideLUT'


class Spouseetclut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpouseEtcLUT'


class Stage1Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stage1LUT'


class Stage2Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stage2LUT'


class Stagelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StageLUT'


class Stateatdeathlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateAtDeathLUT'


class Stateofmetslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateOfMetsLUT'


class Stateofnodeslut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateOfNodesLUT'


class Stateofprimarylut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateOfPrimaryLUT'


class Surgerycompletelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SurgeryCompleteLUT'


class Surgical(models.Model):
    index = models.TextField(primary_key=True)
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    episode = models.IntegerField(db_column='EPISODE', blank=True, null=True)  # Field name made lowercase.
    sudate = models.TextField(db_column='SUDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    susite = models.TextField(db_column='SUSITE', blank=True, null=True)  # Field name made lowercase.
    suoper = models.FloatField(db_column='SUOPER', blank=True, null=True)  # Field name made lowercase.
    sucomp = models.FloatField(db_column='SUCOMP', blank=True, null=True)  # Field name made lowercase.
    sutnm1 = models.TextField(db_column='SUTNM1', blank=True, null=True)  # Field name made lowercase.
    sutnm2 = models.TextField(db_column='SUTNM2', blank=True, null=True)  # Field name made lowercase.
    sutnm3 = models.TextField(db_column='SUTNM3', blank=True, null=True)  # Field name made lowercase.
    sutnm4 = models.TextField(db_column='SUTNM4', blank=True, null=True)  # Field name made lowercase.
    sutnm5 = models.TextField(db_column='SUTNM5', blank=True, null=True)  # Field name made lowercase.
    sutnm6 = models.TextField(db_column='SUTNM6', blank=True, null=True)  # Field name made lowercase.
    sutnm_t = models.TextField(db_column='SUTNM_T', blank=True, null=True)  # Field name made lowercase.
    sutnm_n = models.TextField(db_column='SUTNM_N', blank=True, null=True)  # Field name made lowercase.
    sutnm_m = models.TextField(db_column='SUTNM_M', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Surgical'


class T1Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T1LUT'


class T2Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T2LUT'


class Tlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TLUT'


class Tnmforrtlut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TNMForRTLUT'


class Tvaluelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TValueLUT'


class Techniquelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.
    fields = models.TextField(db_column='Fields', blank=True, null=True)  # Field name made lowercase.
    shape = models.TextField(db_column='Shape', blank=True, null=True)  # Field name made lowercase.
    wedged = models.TextField(db_column='Wedged', blank=True, null=True)  # Field name made lowercase.
    shell = models.TextField(db_column='Shell', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TechniqueLUT'


class Treatmentstate2Lut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreatmentState2LUT'


class Treatmentstatelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreatmentStateLUT'


class Treatmenttypelut(models.Model):
    index = models.TextField(primary_key=True)
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    meaning = models.TextField(db_column='Meaning', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TreatmentTypeLUT'


class Maindata(models.Model):
    index = models.TextField(primary_key=True)
    dco = models.IntegerField(db_column='DCO', blank=True, null=True)  # Field name made lowercase.
    patient = models.IntegerField(db_column='PATIENT', blank=True, null=True)  # Field name made lowercase.
    primary = models.IntegerField(db_column='PRIMARY', blank=True, null=True)  # Field name made lowercase.
    fsdate = models.TextField(db_column='FSDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uhpi = models.TextField(db_column='UHPI', blank=True, null=True)  # Field name made lowercase.
    uhpiold = models.TextField(db_column='UHPIold', blank=True, null=True)  # Field name made lowercase.
    wghnum = models.TextField(db_column='WGHNUM', blank=True, null=True)  # Field name made lowercase.
    idstatus = models.TextField(db_column='IDstatus', blank=True, null=True)  # Field name made lowercase.
    fsc2date = models.TextField(db_column='FSC2DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iopat = models.TextField(db_column='IOPAT', blank=True, null=True)  # Field name made lowercase.
    anndate = models.TextField(db_column='ANNDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    site = models.TextField(db_column='SITE', blank=True, null=True)  # Field name made lowercase.
    side = models.IntegerField(db_column='SIDE', blank=True, null=True)  # Field name made lowercase.
    histol = models.TextField(db_column='HISTOL', blank=True, null=True)  # Field name made lowercase.
    histol3 = models.TextField(db_column='HISTOL3', blank=True, null=True)  # Field name made lowercase.
    trtst1 = models.TextField(db_column='TRTST1', blank=True, null=True)  # Field name made lowercase.
    trtst2 = models.TextField(db_column='TRTST2', blank=True, null=True)  # Field name made lowercase.
    stage = models.TextField(db_column='STAGE', blank=True, null=True)  # Field name made lowercase.
    tnm_t = models.TextField(db_column='TNM_T', blank=True, null=True)  # Field name made lowercase.
    tnm_n = models.TextField(db_column='TNM_N', blank=True, null=True)  # Field name made lowercase.
    tnm_m = models.TextField(db_column='TNM_M', blank=True, null=True)  # Field name made lowercase.
    tumsize = models.FloatField(db_column='TUMSIZE', blank=True, null=True)  # Field name made lowercase.
    perfstat = models.TextField(db_column='PERFSTAT', blank=True, null=True)  # Field name made lowercase.
    parity1 = models.TextField(db_column='PARITY1', blank=True, null=True)  # Field name made lowercase.
    parity2 = models.TextField(db_column='PARITY2', blank=True, null=True)  # Field name made lowercase.
    lmp = models.TextField(db_column='LMP', blank=True, null=True)  # Field name made lowercase.
    siten11 = models.TextField(db_column='SITEN11', blank=True, null=True)  # Field name made lowercase.
    siten12 = models.TextField(db_column='SITEN12', blank=True, null=True)  # Field name made lowercase.
    siten21 = models.TextField(db_column='SITEN21', blank=True, null=True)  # Field name made lowercase.
    siten22 = models.TextField(db_column='SITEN22', blank=True, null=True)  # Field name made lowercase.
    siten31 = models.TextField(db_column='SITEN31', blank=True, null=True)  # Field name made lowercase.
    siten32 = models.TextField(db_column='SITEN32', blank=True, null=True)  # Field name made lowercase.
    sizenod1 = models.TextField(db_column='SIZENOD1', blank=True, null=True)  # Field name made lowercase.
    sizenod2 = models.TextField(db_column='SIZENOD2', blank=True, null=True)  # Field name made lowercase.
    sizenod3 = models.TextField(db_column='SIZENOD3', blank=True, null=True)  # Field name made lowercase.
    sitemet1 = models.TextField(db_column='SITEMET1', blank=True, null=True)  # Field name made lowercase.
    sitemet2 = models.TextField(db_column='SITEMET2', blank=True, null=True)  # Field name made lowercase.
    sitemet3 = models.TextField(db_column='SITEMET3', blank=True, null=True)  # Field name made lowercase.
    notreat = models.TextField(db_column='NOTREAT', blank=True, null=True)  # Field name made lowercase.
    curdate = models.TextField(db_column='CURDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dod = models.TextField(db_column='DOD', blank=True, null=True)  # Field name made lowercase.
    datdeath = models.TextField(db_column='DATDEATH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stadeath = models.FloatField(db_column='STADEATH', blank=True, null=True)  # Field name made lowercase.
    caudeath = models.FloatField(db_column='CAUDEATH', blank=True, null=True)  # Field name made lowercase.
    pmprim = models.TextField(db_column='PMPRIM', blank=True, null=True)  # Field name made lowercase.
    pmnodes = models.TextField(db_column='PMNODES', blank=True, null=True)  # Field name made lowercase.
    pmmeta = models.TextField(db_column='PMMETA', blank=True, null=True)  # Field name made lowercase.
    pmnprim = models.TextField(db_column='PMNPRIM', blank=True, null=True)  # Field name made lowercase.
    pfndtrt1 = models.TextField(db_column='PFNDTRT1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    psite1 = models.TextField(db_column='PSITE1', blank=True, null=True)  # Field name made lowercase.
    ptnm1_t = models.TextField(db_column='PTNM1_T', blank=True, null=True)  # Field name made lowercase.
    ptnm1_n = models.TextField(db_column='PTNM1_N', blank=True, null=True)  # Field name made lowercase.
    ptnm1_m = models.TextField(db_column='PTNM1_M', blank=True, null=True)  # Field name made lowercase.
    ptreat1 = models.FloatField(db_column='PTREAT1', blank=True, null=True)  # Field name made lowercase.
    pfndtrt2 = models.TextField(db_column='PFNDTRT2', blank=True, null=True)  # Field name made lowercase.
    psite2 = models.TextField(db_column='PSITE2', blank=True, null=True)  # Field name made lowercase.
    ptnm2_t = models.TextField(db_column='PTNM2_T', blank=True, null=True)  # Field name made lowercase.
    ptnm2_n = models.TextField(db_column='PTNM2_N', blank=True, null=True)  # Field name made lowercase.
    ptnm2_m = models.TextField(db_column='PTNM2_M', blank=True, null=True)  # Field name made lowercase.
    ptreat2 = models.TextField(db_column='PTREAT2', blank=True, null=True)  # Field name made lowercase.
    pfndtrt3 = models.TextField(db_column='PFNDTRT3', blank=True, null=True)  # Field name made lowercase.
    psite3 = models.TextField(db_column='PSITE3', blank=True, null=True)  # Field name made lowercase.
    ptnm3_t = models.TextField(db_column='PTNM3_T', blank=True, null=True)  # Field name made lowercase.
    ptnm3_n = models.TextField(db_column='PTNM3_N', blank=True, null=True)  # Field name made lowercase.
    ptnm3_m = models.TextField(db_column='PTNM3_M', blank=True, null=True)  # Field name made lowercase.
    ptreat3 = models.TextField(db_column='PTREAT3', blank=True, null=True)  # Field name made lowercase.
    pfndtrt4 = models.TextField(db_column='PFNDTRT4', blank=True, null=True)  # Field name made lowercase.
    psite4 = models.TextField(db_column='PSITE4', blank=True, null=True)  # Field name made lowercase.
    ptnm4_t = models.TextField(db_column='PTNM4_T', blank=True, null=True)  # Field name made lowercase.
    ptnm4_n = models.TextField(db_column='PTNM4_N', blank=True, null=True)  # Field name made lowercase.
    ptnm4_m = models.TextField(db_column='PTNM4_M', blank=True, null=True)  # Field name made lowercase.
    ptreat4 = models.TextField(db_column='PTREAT4', blank=True, null=True)  # Field name made lowercase.
    fuspt = models.FloatField(db_column='FUSPT', blank=True, null=True)  # Field name made lowercase.
    fuslrn = models.FloatField(db_column='FUSLRN', blank=True, null=True)  # Field name made lowercase.
    firptdt = models.TextField(db_column='FIRPTDT', blank=True, null=True)  # Field name made lowercase.
    firlrndt = models.TextField(db_column='FIRLRNDT', blank=True, null=True)  # Field name made lowercase.
    firmetdt = models.TextField(db_column='FIRMETDT', blank=True, null=True)  # Field name made lowercase.
    firlmdt = models.TextField(db_column='FIRLMDT', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.
    reminder = models.TextField(db_column='REMINDER', blank=True, null=True)  # Field name made lowercase.
    reminddate = models.TextField(db_column='REMINDDATE', blank=True, null=True)  # Field name made lowercase.
    epi08 = models.TextField(db_column='EPI08', blank=True, null=True)  # Field name made lowercase.
    epi09 = models.TextField(db_column='EPI09', blank=True, null=True)  # Field name made lowercase.
    epi10 = models.TextField(db_column='EPI10', blank=True, null=True)  # Field name made lowercase.
    epi11 = models.TextField(db_column='EPI11', blank=True, null=True)  # Field name made lowercase.
    epi12 = models.TextField(db_column='EPI12', blank=True, null=True)  # Field name made lowercase.
    epi13 = models.TextField(db_column='EPI13', blank=True, null=True)  # Field name made lowercase.
    epi14 = models.TextField(db_column='EPI14', blank=True, null=True)  # Field name made lowercase.
    epi15 = models.TextField(db_column='EPI15', blank=True, null=True)  # Field name made lowercase.
    epi16 = models.TextField(db_column='EPI16', blank=True, null=True)  # Field name made lowercase.
    epi17 = models.TextField(db_column='EPI17', blank=True, null=True)  # Field name made lowercase.
    epi18 = models.TextField(db_column='EPI18', blank=True, null=True)  # Field name made lowercase.
    epi19 = models.TextField(db_column='EPI19', blank=True, null=True)  # Field name made lowercase.
    epi20 = models.TextField(db_column='EPI20', blank=True, null=True)  # Field name made lowercase.
    epi21 = models.TextField(db_column='EPI21', blank=True, null=True)  # Field name made lowercase.
    epi22 = models.TextField(db_column='EPI22', blank=True, null=True)  # Field name made lowercase.
    tnm1 = models.TextField(db_column='TNM1', blank=True, null=True)  # Field name made lowercase.
    tnm2 = models.TextField(db_column='TNM2', blank=True, null=True)  # Field name made lowercase.
    tnm3 = models.TextField(db_column='TNM3', blank=True, null=True)  # Field name made lowercase.
    tnm4 = models.TextField(db_column='TNM4', blank=True, null=True)  # Field name made lowercase.
    tnm5 = models.TextField(db_column='TNM5', blank=True, null=True)  # Field name made lowercase.
    tnm6 = models.TextField(db_column='TNM6', blank=True, null=True)  # Field name made lowercase.
    histol1 = models.TextField(db_column='HISTOL1', blank=True, null=True)  # Field name made lowercase.
    histol2 = models.TextField(db_column='HISTOL2', blank=True, null=True)  # Field name made lowercase.
    stage1 = models.TextField(db_column='STAGE1', blank=True, null=True)  # Field name made lowercase.
    stage2 = models.TextField(db_column='STAGE2', blank=True, null=True)  # Field name made lowercase.
    ptnm11 = models.TextField(db_column='PTNM11', blank=True, null=True)  # Field name made lowercase.
    ptnm12 = models.TextField(db_column='PTNM12', blank=True, null=True)  # Field name made lowercase.
    ptnm13 = models.TextField(db_column='PTNM13', blank=True, null=True)  # Field name made lowercase.
    ptnm14 = models.TextField(db_column='PTNM14', blank=True, null=True)  # Field name made lowercase.
    ptnm15 = models.TextField(db_column='PTNM15', blank=True, null=True)  # Field name made lowercase.
    ptnm16 = models.TextField(db_column='PTNM16', blank=True, null=True)  # Field name made lowercase.
    ptnm21 = models.TextField(db_column='PTNM21', blank=True, null=True)  # Field name made lowercase.
    ptnm22 = models.TextField(db_column='PTNM22', blank=True, null=True)  # Field name made lowercase.
    ptnm23 = models.TextField(db_column='PTNM23', blank=True, null=True)  # Field name made lowercase.
    ptnm24 = models.TextField(db_column='PTNM24', blank=True, null=True)  # Field name made lowercase.
    ptnm25 = models.TextField(db_column='PTNM25', blank=True, null=True)  # Field name made lowercase.
    ptnm26 = models.TextField(db_column='PTNM26', blank=True, null=True)  # Field name made lowercase.
    ptnm31 = models.TextField(db_column='PTNM31', blank=True, null=True)  # Field name made lowercase.
    ptnm32 = models.TextField(db_column='PTNM32', blank=True, null=True)  # Field name made lowercase.
    ptnm33 = models.TextField(db_column='PTNM33', blank=True, null=True)  # Field name made lowercase.
    ptnm34 = models.TextField(db_column='PTNM34', blank=True, null=True)  # Field name made lowercase.
    ptnm35 = models.TextField(db_column='PTNM35', blank=True, null=True)  # Field name made lowercase.
    ptnm36 = models.TextField(db_column='PTNM36', blank=True, null=True)  # Field name made lowercase.
    ptnm41 = models.TextField(db_column='PTNM41', blank=True, null=True)  # Field name made lowercase.
    ptnm42 = models.TextField(db_column='PTNM42', blank=True, null=True)  # Field name made lowercase.
    ptnm43 = models.TextField(db_column='PTNM43', blank=True, null=True)  # Field name made lowercase.
    ptnm44 = models.TextField(db_column='PTNM44', blank=True, null=True)  # Field name made lowercase.
    ptnm45 = models.TextField(db_column='PTNM45', blank=True, null=True)  # Field name made lowercase.
    ptnm46 = models.TextField(db_column='PTNM46', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maindata'
