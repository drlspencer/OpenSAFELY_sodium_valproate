from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv, combine_codelists, filter_codes_by_category  # NOQA
# from datetime import date
# from codelists import *  # <- if we need to collect codelists in one place
# to update codelists: run 'opensafeley codelists update'

# ---------- OVERALL CODE DEFINITIONS

teratogenic_drug_codes = codelist_from_csv(
    "codelists/opensafely-teratogenic-medicines.csv",
    system="snomed",
    column="dmd_id")

# use the following if we want to restrict to specific codes, 
# e.g. for only sodium valproate:
# weight_codes = codelist(
#    ["27113001", "162763007"], system="snomed"
# )

# seizure_frequency_codes = codelist_from_csv(
#    "codelists/nhsd-primary-care-domain-refsets-lszfreq_cod.csv",
#    system="snomed",
#    column="dmd_id")

# set date variable to current date
index_date = '2022-01-01'
# str(date.today()),

# ---------- SET VARIABLES

# This is used to set default behaviour for the dummy data that is generated.
# In this case, we expect event dates to be between 1950-01-01 and today's
# date, uniformly distributed in that period, and to be recorded for 50%
# of patients (returning empty "" values otherwise).
study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1950-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    # population=patients.registered_with_one_practice_between(
    #     "2019-02-01", "2020-02-01"
    # ),

    population=patients.all(),

    age=patients.age_as_of(
        index_date,
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),

    imd=patients.address_as_of(
        index_date,
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        }
    ),

        # return_expectations={
           # "int": {"distribution": "normal", "mean": 2, "stddev": 1},
           # "incidence": 0.2,
        # },

    TMcode=patients.with_these_medications(
        teratogenic_drug_codes,
        return_expectations=None,
        on_or_before=None,
        on_or_after=None,
        between=None,
        find_first_match_in_period=None,
        find_last_match_in_period=None,
        returning='binary flag',
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
