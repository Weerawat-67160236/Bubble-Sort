class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def display(self):
        print("Current data:", self.data)

    def sort(self):
        n = len(self.data)
        for i in range(n - 1):
# วนรอบเปรียบเทียบค่าแต่ละคู่
            for j in range(n - 1 - i):
                if self.data[j] > self.data[j + 1]:
# สลับค่า
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
            print(f"After round {i + 1}: {self.data}")
        print("Sorting complete!\n")


# ------------------------------
# ส่วนทดสอบการทำงานของโปรแกรม
# ------------------------------
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSorter(nums)

    print("Before sorting:")
    sorter.display()

    sorter.sort()

    print("After sorting:")
    sorter.display()