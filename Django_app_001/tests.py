from django.test import TestCase

# Create your tests here.
from Django_app_001.models import CPU_memory_utli
import random
import time

for i in range(50):
    a = CPU_memory_utli(
                        device_name='CSR100V_1',
                        device_ip='172.1.1.1',
                        cpu_utli=random.randint(0, 100),
                        memory_utli=random.randint(0, 100)
                        )
    time.sleep(random.randint(1,15))
    a.save()
