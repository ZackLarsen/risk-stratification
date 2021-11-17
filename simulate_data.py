"""
Using Faker to simulate data
"""

import numpy as np
import pandas as pd

from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()


age_provider = DynamicProvider(
    provider_name="age",
    elements=[x for x in range(1,100)],
)

fake.add_provider(age_provider)




gender_provider = DynamicProvider(
    provider_name="gender",
    elements=['male', 'female'],
)

fake.add_provider(gender_provider)



product_code_provider = DynamicProvider(
    provider_name="product",
    elements=['DCFS', 'MMAI', 'FHP-ACA', 'FHP-NONACA', 'SNC', 'MLTSS'],
)

fake.add_provider(product_code_provider)





#https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2022/
icd10_diagnosis_code_provider = DynamicProvider(
    provider_name="diagnosis",
    elements=[],
)

fake.add_provider(icd10_diagnosis_code_provider)









fake.name()


fake.medical_profession()


fake.product()


fake.age()


fake.gender()
