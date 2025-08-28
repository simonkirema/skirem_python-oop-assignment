
---

## 📂 assignment1/smartphone.py  

```python
# Assignment 1: Design Your Own Class 🏗️

# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage   # Encapsulation with protected attribute
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")
    
    def get_storage(self):
        return f"Storage: {self._storage}GB"


# Child Class (inherits Smartphone)
class SmartCameraPhone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels
    
    def take_photo(self):
        print(f"{self.brand} {self.model} takes a {self.camera_megapixels}MP photo 📸")


# Testing the classes
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S21", 128)
    phone2 = SmartCameraPhone("Apple", "iPhone 14", 256, 48)

    phone1.call("0712345678")
    print(phone1.get_storage())

    phone2.call("0798765432")
    phone2.take_photo()
    print(phone2.get_storage())
