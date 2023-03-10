from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
# from codelists import *

teratogenic_drug_codes = codelist_from_csv(
    "codelists/opensafely-teratogenic-medicines.csv",
    system="snomed",
    column="dmd_id")

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    # population=patients.registered_with_one_practice_between(
    #     "2019-02-01", "2020-02-01"
    # ),

    population=patients.all(),

    age=patients.age_as_of(
        "2022-09-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

    example=patients.with_these_medications(
        teratogenic_drug_codes,
        return_expectations={
           "int": {"distribution": "normal", "mean": 2, "stddev": 1},
           "incidence": 0.2,
        },
        on_or_before=None,
        on_or_after=None,
        between=None,
        find_first_match_in_period=None,
        find_last_match_in_period=None,
        returning='binary_flag',
        include_date_of_match=True,
        date_format=None,
        ignore_days_where_these_clinical_codes_occur=None,
        episode_defined_as=None,
        return_binary_flag=None,
        return_number_of_matches_in_period=False,
        return_first_date_in_period=False,
        return_last_date_in_period=False,
        include_month=False,
        include_day=False)
)
