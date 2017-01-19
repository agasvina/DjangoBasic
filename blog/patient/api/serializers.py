from rest_framework import serializers
from patient.models import (
    Followup,
    Futypelut,

    Surgical,
    Surgerycompletelut,

    Maindata, #For Death & Diagnosis.
    Performancestatuslut,

    Sitelut,

    Radiotherapy,
    Techniquelut,
    Radicalpalliativelut,

    Hormone,
    Hormonemateriallut,
    Hormonemethodlut,
)

class FollowupModelSerializer(serializers.ModelSerializer):
    futype = serializers.SlugRelatedField(read_only=True, slug_field='meaning')

    class Meta:
        model = Followup
        fields = [
            'index',
            'patient',
            'primary',
            'episode',
            'fudate',
            'futype',
        ]

class SurgicalModelSerializer(serializers.ModelSerializer):
    site = serializers.SerializerMethodField('get_site_meaning')
    completed = serializers.SerializerMethodField('is_completed')

    def get_site_meaning(self, instance):
        try:
            return Sitelut.objects.get(code=instance.susite).meaning
        except:
            print("Site-Not-Found")
        return "Unknown"

    def is_completed(self, instance):
        try:
            return Surgerycompletelut.objects.get(code=instance.sucomp).meaning
        except:
            print("Completed not found")
        return "Unknown"

    class Meta:
        model = Surgical
        fields = [
            'index',
            'patient',
            'episode',
            'sudate',
            'site',
            'completed',
        ]

#For DIAGNOSIS & Death:
class MaindataModelSerializer(serializers.ModelSerializer):
    siteMeaning = serializers.SerializerMethodField('get_site_meaning')
    performanceStatus = serializers.SerializerMethodField('get_performance')
    stateOfDeath = serializers.SerializerMethodField('get_state_of_death')

    #TODO: Create better for avoid this F***-ing repeatation...
    def get_site_meaning(self, instance):
        try:
            return Sitelut.objects.get(code=instance.site).meaning
        except:
            print("Site not Found")

        return "Unknown"

    def get_performance(self, instance):
        try:
            return Performancestatuslut.objects.get(code=instance.perfstat).meaning
        except:
            print("Performance not found")
        return "Unknown"

    def get_state_of_death(self, instance):
        try:
            return Stateatdeathlut.objects.get(code=instance.stadeath).meaning
        except:
            print("State of Death not found")
        return "Unknown"

    class Meta:
        model = Maindata
        fields = [
            'index',
            #BOTH:
            'patient',
            'primary',
            #DIAGNOSIS:
            'anndate',
            'siteMeaning',
            'performanceStatus',
            'stage',

            #DEATH:
            'datdeath',
            'stateOfDeath',
        ]

class HormoneModelSerializer(serializers.ModelSerializer):
    material = serializers.SerializerMethodField('get_material_explaination')
    method = serializers.SerializerMethodField('get_method_explaination')

    def get_material_explaination(self, instance):
        try:
            return Hormonemateriallut.objects.get(code=instance.material).meaning
        except:
            print("Material not found")
        return "Unknown"

    def get_method_explaination(self, instance):
        try:
            return Hormonemethodlut.objects.get(code=instance.method).meaning
        except:
            print("Method not found")
        return "Unknown"

    class Meta:
        model = Hormone
        fields = [
            'index',
            'patient',
            'primary',
            'episode',
            'stdate',
            'enddate',
            'material',
            'method',
        ]

class RadiotherapyModelSerializer(serializers.ModelSerializer):
    tech = serializers.SerializerMethodField('get_tech_explaination')
    radpall = serializers.SerializerMethodField('get_radpall_explaination')

    def get_tech_explaination(self, instance):
        try:
            return Techniquelut.objects.get(code=instance.tech).meaning
        except:
            print("Technique not found")
        return "Unknown"

    def get_radpall_explaination(self, instance):
        try:
            return Radicalpalliativelut.objects.get(code=instance.radpall).meaning
        except:
            print("Rad-Pall not found")
        return "Unknown"

    class Meta:
        model = Radiotherapy
        fields = [
            'index',
            'primary',
            'patient',
            'episode',
            'stdate',
            'enddate',
            'tech',
            'radpall',
        ]


