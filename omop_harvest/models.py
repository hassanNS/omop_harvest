from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
<<<<<<< HEAD
    gender_concept = models.ForeignKey('PersonGenderConcept')
    year_of_birth = models.DecimalField(max_digits=4, decimal_places=0, help_text='The year of birth of the Person. For data sources with date of birth, only the year is extracted. For data sources where the year of birth is not available, the approximate year of birth is derived based on any age group categorization available.')
    month_of_birth = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True, help_text='The month of birth of the person. For data sources that provide the precise date of birth, the month is extracted and stored in this field.')
    day_of_birth = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True, help_text='The day of the month of birth of the person. For data sources that provide the precise date of birth, the day is extracted and stored in this field.')
    race_concept = models.ForeignKey('PersonRaceConcept', null=True, blank=True)
    ethnicity_concept = models.ForeignKey('PersonEthnicityConcept', null=True, blank=True)
    location_id = models.IntegerField(null=True, blank=True)
    provider_id = models.IntegerField(null=True, blank=True)
    care_site_id = models.IntegerField(null=True, blank=True)
    person_source_value = models.CharField(max_length=50, blank=True, help_text='An encrypted key derived from the person identifier in the source data. This is necessary when a drug safety issue requires a link back to the person data at the source dataset. No value with any medical or demographic significance must be stored.')
    gender_source_value = models.CharField(max_length=50, blank=True, help_text='The source code for the gender of the person as it appears in the source data. The person gender is mapped to a standard gender concept in the vocabulary and the corresponding concept identifier is, stored here for reference.')
    race_source_value = models.CharField(max_length=50, blank=True, help_text='The source code for the race of the person as it appears in the source data. The person race is mapped to a standard race concept in the vocabulary and the original code is, stored here for reference.')
    ethnicity_source_value = models.CharField(max_length=50, blank=True, help_text='The source code for the ethnicity of the person as it appears in the source data. The person ethnicity is mapped to a standard ethnicity concept in the vocabulary and the original code is, stored here for reference.')
    location_concept = models.ForeignKey('PersonLocationConcept', null=True, blank=True)
    source_location_code = models.CharField(max_length=50, blank=True, help_text='Deprecated CDMV2 field to store source location values. Locations are now stored in the location table.')
    class Meta:
        db_table = 'omop_person'

class ObservationPeriod(models.Model):
    observation_period_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Person')
    observation_period_start_date = models.DateField(help_text='The start date of the observation period for which data are available from the data source.')
    observation_period_end_date = models.DateField(help_text='The end date of the observation period for which data are available from the data source.')
    person_status_concept = models.ForeignKey('ObservationPeriodPersonStatusConcept', null=True, blank=True)
    rx_data_availability = models.CharField(max_length=1, blank=True, help_text='Deprecated CDMV2 field that tracks the availability of prescription data for the observation period.')
    dx_data_availability = models.CharField(max_length=1, blank=True, help_text='Deprecated CDMV2 field that tracks the availability of diagnosis data for the observation period.')
    hospital_data_availability = models.CharField(max_length=1, blank=True, help_text='Deprecated CDMV2 field recording the availability of hospital data for the observation period.')
    confidence = models.NullBooleanField(null=True, blank=True, help_text='Deprecated CDMV2 field.')
    class Meta:
        db_table = 'omop_observation_period'

class DrugEra(models.Model):
    drug_era_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Person')
    drug_concept = models.ForeignKey('DrugEraDrugConcept')
    drug_era_start_date = models.DateField(help_text='The start date for the drug era constructed from the individual instances of drug exposures. It is the start date of the very first chronologically recorded instance of utilization of a drug.')
    drug_era_end_date = models.DateField(help_text='The end date for the drug era constructed from the individual instance of drug exposures. It is the end date of the final continuously recorded instance of utilization of a drug.')
    drug_type_concept_id = models.IntegerField()
    drug_exposure_count = models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True, help_text='The number of individual drug exposure occurrences used to construct the drug era.')
    class Meta:
        db_table = 'omop_drug_era'

class ConditionEra(models.Model):
    condition_era_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Person')
    condition_concept = models.ForeignKey('ConditionEraConditionConcept')
    condition_era_start_date = models.DateField(help_text='The start date for the condition era constructed from the individual instances of condition occurrences. It is the start date of the very first chronologically recorded instance of the condition.')
    condition_era_end_date = models.DateField(help_text='The end date for the condition era constructed from the individual instances of condition occurrences. It is the end date of the final continuously recorded instance of the condition.')
    condition_type_concept_id = models.IntegerField()
    condition_occurrence_count = models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True, help_text='The number of individual condition occurrences used to construct the condition era.')
    confidence = models.NullBooleanField(null=True, blank=True, help_text='Deprecated CDMV2 field.')
    class Meta:
        db_table = 'omop_condition_era'

class PersonGenderConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_person_gender_concept'

class PersonRaceConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_person_race_concept'

class PersonEthnicityConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_person_ethnicity_concept'

class PersonLocationConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_person_location_concept'

class ObservationPeriodPersonStatusConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_observation_period_person_status_concept'

class DrugEraDrugConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_drug_era_drug_concept'

class ConditionEraConditionConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256, help_text='An unambiguous, meaningful and descriptive name for the concept.')
    concept_level = models.IntegerField(help_text='The level of hierarchy associated with the concept. Different concept levels are assigned to concepts to depict their seniority in a clearly defined hierarchy, such as drugs, conditions, etc. A concept level of 0 is assigned to concepts that are not part of a standard vocabulary, but are part of the vocabulary for reference purposes (e.g. drug form).')
    concept_class = models.CharField(max_length=60, help_text='The category or class of the concept along both the hierarchical tree as well as different domains within a vocabulary. Examples are \'Clinical Drug\', \'Ingredient\', \'Clinical Finding\' etc.')
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40, help_text='The concept code represents the identifier of the concept in the source data it originates from, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.')
    valid_start_date = models.DateField(help_text='The date when the was first recorded.')
    valid_end_date = models.DateField(help_text='The date when the concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099.')
    invalid_reason = models.CharField(max_length=1, blank=True, help_text='Concepts that are replaced with a new concept are designated \'Updated\' (U) and concepts that are removed without replacement are \'Deprecated\' (D).')
    class Meta:
        managed = False
        db_table = 'omop_condition_era_condition_concept'

=======
    gender_concept = models.ForeignKey('Gender', null=True, blank=True)
    year_of_birth = models.DecimalField(max_digits=4, decimal_places=0)
    month_of_birth = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True)
    day_of_birth = models.DecimalField(null=True, max_digits=2, decimal_places=0, blank=True)
    race_concept = models.ForeignKey('Race', null=True, blank=True)
    ethnicity_concept = models.ForeignKey('Ethnicity', null=True, blank=True)
    location = models.ForeignKey('PersonLocation', null=True, blank=True)
    provider = models.ForeignKey('Provider', null=True, blank=True)
    care_site = models.ForeignKey('CareSite', null=True, blank=True)
    person_source_value = models.CharField(max_length=50, blank=True)
    gender_source_value = models.CharField(max_length=50, blank=True)
    race_source_value = models.CharField(max_length=50, blank=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'person'

class Gender(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'gender'

class Race(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'race'

class Ethnicity(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'ethnicity'

class PersonLocation(models.Model):
    location_id = models.IntegerField(primary_key=True)
    address_1 = models.CharField(max_length=50, blank=True)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=9, blank=True)
    county = models.CharField(max_length=20, blank=True)
    location_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'person_location'

class Provider(models.Model):
    provider_id = models.IntegerField(primary_key=True)
    npi = models.CharField(max_length=20, blank=True)
    dea = models.CharField(max_length=20, blank=True)
    specialty_concept = models.ForeignKey('ProviderSpecialty', null=True, blank=True)
    care_site_id = models.IntegerField(null=True, blank=True)
    provider_source_value = models.CharField(max_length=50)
    specialty_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'provider'

class ProviderSpecialty(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'provider_specialty'

class CareSite(models.Model):
    care_site_id = models.IntegerField(primary_key=True)
    location = models.ForeignKey('CareSiteLocation', null=True, blank=True)
    organization = models.ForeignKey('Organization', null=True, blank=True)
    place_of_service_concept = models.ForeignKey('CareSitePOS', null=True, blank=True)
    care_site_source_value = models.CharField(max_length=50, blank=True)
    place_of_service_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'care_site'

class CareSiteLocation(models.Model):
    location_id = models.IntegerField(primary_key=True)
    address_1 = models.CharField(max_length=50, blank=True)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=9, blank=True)
    county = models.CharField(max_length=20, blank=True)
    location_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'care_site_location'

class Organization(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    place_of_service_concept_id = models.IntegerField(null=True, blank=True)
    location_id = models.IntegerField(null=True, blank=True)
    organization_source_value = models.CharField(max_length=50, blank=True)
    place_of_service_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'organization'

class CareSitePOS(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'care_site_pos'

class Visit(models.Model):
    visit_occurrence_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Person')
    visit_start_date = models.DateTimeField()
    visit_end_date = models.DateTimeField()
    place_of_service_concept_id = models.IntegerField()
    care_site_id = models.IntegerField(null=True, blank=True)
    place_of_service_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'visit_occurrence'

class VisitCondition(models.Model):
    condition_occurrence_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    condition_concept = models.ForeignKey('VisitConditionConcept')
    condition_start_date = models.DateTimeField()
    condition_end_date = models.DateTimeField(null=True, blank=True)
    condition_type_concept = models.ForeignKey('VisitConditionType')
    stop_reason = models.CharField(max_length=20, blank=True)
    associated_provider_id = models.IntegerField(null=True, blank=True)
    visit_occurrence = models.ForeignKey('Visit', null=True, blank=True)
    condition_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'visit_condition'

class VisitConditionConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'visit_condition_concept'

class VisitConditionType(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'visit_condition_type'

class VisitProcedure(models.Model):
    procedure_occurrence_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    procedure_concept = models.ForeignKey('VisitProcedureConcept')
    procedure_date = models.DateTimeField()
    procedure_type_concept = models.ForeignKey('VisitProcedureType')
    associated_provider_id = models.IntegerField(null=True, blank=True)
    visit_occurrence = models.ForeignKey('Visit', null=True, blank=True)
    relevant_condition_concept_id = models.IntegerField(null=True, blank=True)
    procedure_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'visit_procedure'

class VisitProcedureConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'visit_procedure_concept'

class VisitProcedureType(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'visit_procedure_type'

class VisitDrug(models.Model):
    drug_exposure_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    drug_concept = models.ForeignKey('VisitDrugConcept')
    drug_exposure_start_date = models.DateTimeField()
    drug_exposure_end_date = models.DateTimeField(null=True, blank=True)
    drug_type_concept = models.ForeignKey('VisitDrugType')
    stop_reason = models.CharField(max_length=20, blank=True)
    refills = models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)
    quantity = models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)
    days_supply = models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)
    sig = models.CharField(max_length=500, blank=True)
    prescribing_provider_id = models.IntegerField(null=True, blank=True)
    visit_occurrence = models.ForeignKey('Visit', null=True, blank=True)
    relevant_condition_concept_id = models.IntegerField(null=True, blank=True)
    drug_source_value = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'visit_drug'

class VisitDrugConcept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'visit_drug_concept'

class VisitDrugType(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=256)
    concept_level = models.IntegerField()
    concept_class = models.CharField(max_length=60)
    vocabulary_id = models.IntegerField()
    concept_code = models.CharField(max_length=40)
    valid_start_date = models.DateTimeField()
    valid_end_date = models.DateTimeField()
    invalid_reason = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'visit_drug_type'

#class Observation(models.Model):
#    observation_id = models.IntegerField(primary_key=True)
#    person_id = models.ForeignKey('Person')
#    observation_concept_id = models.IntegerField()
#    observation_date = models.DateField()
#    observation_time = models.TimeField(null=True, blank=True)
#    value_as_number = models.DecimalField(null=True, max_digits=14, decimal_places=3, blank=True)
#    value_as_string = models.CharField(max_length=60, blank=True)
#    value_as_concept_id = models.IntegerField(null=True, blank=True)
#    unit_concept_id = models.IntegerField(null=True, blank=True)
#    range_low = models.DecimalField(null=True, max_digits=14, decimal_places=3, blank=True)
#    range_high = models.DecimalField(null=True, max_digits=14, decimal_places=3, blank=True)
#    observation_type_concept_id = models.IntegerField()
#    associated_provider = models.ForeignKey('Provider')
#    visit_occurrence = models.ForeignKey('VisitOccurrence', null=True, blank=True)
#    relevant_condition_concept_id = models.IntegerField(null=True, blank=True)
#    observation_source_value = models.CharField(max_length=50, blank=True)
#    units_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'observation'
#
#class ObservationPeriod(models.Model):
#    observation_period_id = models.IntegerField(primary_key=True)
#    person = models.ForeignKey('Person')
#    observation_period_start_date = models.DateTimeField()
#    observation_period_end_date = models.DateTimeField()
#    class Meta:
#        db_table = 'observation_period'
#
#class PayerPlanPeriod(models.Model):
#    payer_plan_period_id = models.IntegerField(primary_key=True)
#    person = models.ForeignKey('Person')
#    payer_plan_period_start_date = models.DateTimeField()
#    payer_plan_period_end_date = models.DateTimeField()
#    payer_source_value = models.CharField(max_length=50, blank=True)
#    plan_source_value = models.CharField(max_length=50, blank=True)
#    family_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'payer_plan_period'
#
#class Cohort(models.Model):
#    cohort_id = models.IntegerField(primary_key=True)
#    cohort_concept = models.ForeignKey('CohortConcept')
#    cohort_start_date = models.DateTimeField()
#    cohort_end_date = models.DateTimeField(null=True, blank=True)
#    subject = models.ForeignKey('Person')
#    stop_reason = models.CharField(max_length=20, blank=True)
#    class Meta:
#        db_table = 'cohort'
#
#class CohortConcept(models.Model):
#    code = models.IntegerField(primary_key=True, db_column='concept_id')
#    label = models.CharField(max_length=256, db_column='concept_name')
#    concept_level = models.IntegerField()
#    concept_class = models.CharField(max_length=60)
#    vocabulary_id = models.IntegerField()
#    value = models.CharField(max_length=40, db_column='concept_code')
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'cohort_concept'
#
#class ConditionEra(models.Model):
#    condition_era_id = models.IntegerField()
#    person = models.ForeignKey('Person')
#    condition_concept = models.ForeignKey('ConditionEraConcept')
#    condition_era_start_date = models.DateTimeField()
#    condition_era_end_date = models.DateTimeField()
#    condition_type_concept = models.ForeignKey('ConditionEraType')
#    condition_occurrence_count = models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)
#    class Meta:
#        db_table = 'condition_era'
#
#class ConditionEraConcept(models.Model):
#    code = models.IntegerField(primary_key=True, db_column='concept_id')
#    label = models.CharField(max_length=256, db_column='concept_name')
#    concept_level = models.IntegerField()
#    concept_class = models.CharField(max_length=60)
#    vocabulary_id = models.IntegerField()
#    value = models.CharField(max_length=40, db_column='concept_code')
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'condition_era_concept'
#
#class ConditionEraType(models.Model):
#    code = models.IntegerField(primary_key=True, db_column='concept_id')
#    label = models.CharField(max_length=256, db_column='concept_name')
#    concept_level = models.IntegerField()
#    concept_class = models.CharField(max_length=60)
#    vocabulary_id = models.IntegerField()
#    value = models.CharField(max_length=40, db_column='concept_code')
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'condition_era_type'
#
#class ProcedureCost(models.Model):
#    procedure_cost_id = models.IntegerField(primary_key=True)
#    procedure_occurrence = models.ForeignKey('ProcedureOccurrence')
#    paid_copay = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_coinsurance = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_toward_deductible = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_by_payer = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_by_coordination_benefits = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    total_out_of_pocket = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    total_paid = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    disease_class_concept_id = models.IntegerField(null=True, blank=True)
#    revenue_code_concept_id = models.IntegerField(null=True, blank=True)
#    payer_plan_period_id = models.IntegerField(null=True, blank=True)
#    disease_class_source_value = models.CharField(max_length=50, blank=True)
#    revenue_code_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'procedure_cost'
#
#class Death(models.Model):
#    person_death_id = models.IntegerField(primary_key=True)
#    person = models.ForeignKey('Person')
#    death_date = models.DateTimeField()
#    death_type_concept_id = models.IntegerField()
#    cause_of_death_concept_id = models.IntegerField(null=True, blank=True)
#    cause_of_death_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'death'
#
#class DrugApproval(models.Model):
#    ingredient_concept_id = models.IntegerField(primary_key=True)
#    approval_date = models.DateTimeField()
#    approved_by = models.CharField(max_length=20)
#    class Meta:
#        db_table = 'drug_approval'
#
#class DrugCost(models.Model):
#    drug_cost_id = models.IntegerField(primary_key=True)
#    drug_exposure = models.ForeignKey('DrugExposure')
#    paid_copay = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_coinsurance = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_toward_deductible = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_by_payer = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    paid_by_coordination_benefits = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    total_out_of_pocket = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    total_paid = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    ingredient_cost = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    dispensing_fee = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    average_wholesale_price = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
#    payer_plan_period = models.ForeignKey('PayerPlanPeriod', null=True, blank=True)
#    class Meta:
#        db_table = 'drug_cost'
#
#class DrugEra(models.Model):
#    drug_era_id = models.IntegerField(primary_key=True)
#    person = models.ForeignKey('Person')
#    drug_concept_id = models.IntegerField()
#    drug_era_start_date = models.DateTimeField()
#    drug_era_end_date = models.DateTimeField()
#    drug_type_concept_id = models.IntegerField()
#    drug_exposure_count = models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)
#    class Meta:
#        db_table = 'drug_era'
#
#class DrugStrength(models.Model):
#    drug_strength_id = models.IntegerField(primary_key=True)
#    drug_concept_id = models.IntegerField()
#    ingredient_concept_id = models.IntegerField()
#    amount_value = models.DecimalField(null=True, max_digits=50, decimal_places=0, blank=True)
#    amount_unit = models.CharField(max_length=60, blank=True)
#    concentration_value = models.DecimalField(null=True, max_digits=50, decimal_places=0, blank=True)
#    concentration_enum_unit = models.CharField(max_length=60, blank=True)
#    concentration_denom_unit = models.CharField(max_length=60, blank=True)
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'drug_strength'
#
#class Relationship(models.Model):
#    relationship_id = models.IntegerField(primary_key=True)
#    relationship_name = models.CharField(max_length=256)
#    is_hierarchical = models.IntegerField()
#    defines_ancestry = models.IntegerField()
#    reverse_relationship = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = 'relationship'
#
#class SourceToConceptMap(models.Model):
#    source_to_concept_map_id = models.IntegerField(primary_key=True)
#    source_code = models.CharField(max_length=40)
#    source_vocabulary = models.ForeignKey('Vocabulary', related_name='sourcetoconceptmap_targets_set')
#    source_code_description = models.CharField(max_length=256, blank=True)
#    target_concept = models.ForeignKey(Concept)
#    target_vocabulary = models.ForeignKey('Vocabulary', related_name='sourcetoconceptmap_sources_set')
#    mapping_type = models.CharField(max_length=20, blank=True)
#    primary_map = models.CharField(max_length=1, blank=True)
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'source_to_concept_map'
#
#class ConceptAncestor(models.Model):
#    ancestry_id = models.IntegerField(primary_key=True)
#    ancestor_concept = models.ForeignKey('Concept', related_name='conceptancestor_descendents_set')
#    descendant_concept = models.ForeignKey('Concept', related_name='conceptancestor_ancestors_set')
#    max_levels_of_separation = models.IntegerField(null=True, blank=True)
#    min_levels_of_separation = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = 'concept_ancestor'
#
#class ConceptRelationship(models.Model):
#    concept_relationship_id = models.IntegerField(primary_key=True)
#    concept_id_1 = models.ForeignKey('Concept', db_column='concept_id_1', related_name='conceptrelationship_to_set')
#    concept_id_2 = models.ForeignKey('Concept', db_column='concept_id_2', related_name='conceptrelationship_from_set')
#    relationship = models.ForeignKey('Relationship')
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'concept_relationship'
#
#class ConceptSynonym(models.Model):
#    concept_synonym_id = models.IntegerField(primary_key=True)
#    concept = models.ForeignKey('Concept')
#    concept_synonym_name = models.CharField(max_length=1000)
#    class Meta:
#        db_table = 'concept_synonym'
#
#class CareSite(models.Model):
#    care_site_id = models.IntegerField(primary_key=True)
#    location = models.ForeignKey('Location', null=True, blank=True)
#    organization = models.ForeignKey('Organization', null=True, blank=True)
#    place_of_service_concept_id = models.IntegerField(null=True, blank=True)
#    care_site_source_value = models.CharField(max_length=50, blank=True)
#    place_of_service_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'care_site'
#
#class Concept(models.Model):
#    concept_id = models.IntegerField(primary_key=True)
#    concept_name = models.CharField(max_length=256)
#    concept_level = models.IntegerField()
#    concept_class = models.CharField(max_length=60)
#    vocabulary = models.ForeignKey('Vocabulary')
#    concept_code = models.CharField(max_length=40)
#    valid_start_date = models.DateTimeField()
#    valid_end_date = models.DateTimeField()
#    invalid_reason = models.CharField(max_length=1, blank=True)
#    class Meta:
#        db_table = 'concept'
#
#class Organization(models.Model):
#    organization_id = models.IntegerField(primary_key=True)
#    place_of_service_concept_id = models.IntegerField(null=True, blank=True)
#    location = models.ForeignKey('Location', null=True, blank=True)
#    organization_source_value = models.CharField(max_length=50, blank=True)
#    place_of_service_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'organization'
#
#class Location(models.Model):
#    location_id = models.IntegerField(primary_key=True)
#    address_1 = models.CharField(max_length=50, blank=True)
#    address_2 = models.CharField(max_length=50, blank=True)
#    city = models.CharField(max_length=50, blank=True)
#    state = models.CharField(max_length=2, blank=True)
#    zip = models.CharField(max_length=9, blank=True)
#    county = models.CharField(max_length=20, blank=True)
#    location_source_value = models.CharField(max_length=50, blank=True)
#    class Meta:
#        db_table = 'location'
#
#class Vocabulary(models.Model):
#    vocabulary_id = models.IntegerField(primary_key=True)
#    vocabulary_name = models.CharField(max_length=256, unique=True)
#    class Meta:
#        db_table = 'vocabulary'
#
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
