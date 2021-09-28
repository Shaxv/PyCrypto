import datetime

class Crypto():

    # Base

    def __init__(self):
        self.rigmhs = [375, 230, 185, 522, 133, 376, 200, 440, 177, 145, 212, 270, 330]
        self.rigprices = [2700000, 1900000, 1350000, 5000000, 1180000, 2800000, 1500000, 4190000, 1400000, 1300000, 1800000, 2200000, 2700000]
        self.rigsummary = sum(self.rigprices) // sum(self.rigmhs)

        self.gpumhs = [19, 23, 25, 30]
        self.gpuprices = [85000, 115000, 80000, 135000]
        self.gpusummary = sum(self.gpuprices) // sum(self.gpumhs)

    def get_coins(self):
        return print(f"\n There are {len(self.coins)} cryptocoins out there!")

    # Mining

    def get_rig_summary(self):
        return print(f"\nSummary is: {self.rigsummary} Ft for 1 Mh/s! (RIG)")
    
    def get_gpu_summary(self):
        return print(f"\nSummary is: {self.gpusummary} Ft for 1 Mh/s! (GPU)")

    def get_hashrate(self):
        return print(f"1 Mh/s worth 0.1$ / Day or 3.2$ / Month or 39$ / Year")

    def get_rigs(self):
        if len(self.rigmhs) == len(self.rigprices):
            for i in range(len(self.rigmhs)):
                print(f"Rig {i}: {self.rigmhs[i]} Ft. {self.rigprices[i]} Mh/s")
        else:
            print("\nDifferent lenghts")

    def check_rig(self, price, mh):
        rig_summ = price // mh
        if self.rigsummary <= rig_summ:
            print(f"This rig is expensive!")
            print(f"{rig_summ} Mhs / Ft. Cheaper by {self.rigsummary - rig_summ}!")
        else:
            print(f"This rig is a great deal!")
            print(f"{rig_summ} Mhs / Ft. Cheaper by {self.rigsummary - rig_summ}!")
        
    def check_gpu(self, price, mh):
        gpu_summ = price // mh
        if self.gpusummary <= gpu_summ:
            print(f"This gpu is expensive!")
            print(f"{gpu_summ} Mhs / Ft. More expensive by {self.gpusummary - gpu_summ}!")
        else:
            print(f"This gpu is a great deal!")
            print(f"{gpu_summ} Mhs / Ft. Cheaper by {self.gpusummary - gpu_summ}!")

x = Crypto()
x.get_coins()
x.check_gpu(10000, 49)