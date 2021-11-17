"""
Using Faker to simulate data
"""

import numpy as np
import pandas as pd

from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()


fake.name()





medical_professions_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(medical_professions_provider)

# now you can use:
fake.medical_profession()
# 'dr.'
