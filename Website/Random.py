from .models import *
import random

class Genrate_Random_number ():

    i = 0
    main_num = random.randint (i, 5)

    container = Bible_quote.objects.get(pk=main_num)
    print(container)