class FitnessClass:
    def __init__(self, class_name, calorie_per_minute, length, intensity):
        self.class_name = class_name
        self.calorie_per_minute = calorie_per_minute if calorie_per_minute > 0 else 1
        self.length = length if length > 0 else 10
        self.intensity = intensity
        
    def calculate_burn(self):
        return self.calorie_per_minute * self.length
        
kickboxing = FitnessClass(class_name="Kickboxing", calorie_per_minute=10, length=45, intensity="Intermediate")
zumba      = FitnessClass(class_name="Zumba", calorie_per_minute=5, length=60, intensity="Intermediate")
hit        = FitnessClass(class_name="H.I.T", calorie_per_minute=9, length=60, intensity="Hard")
judo       = FitnessClass(class_name="Judo", calorie_per_minute=5, length=45, intensity="Beginner")
dancing    = FitnessClass(class_name="Dancing", calorie_per_minute=10, length=30, intensity="Intermediate")
yoga       = FitnessClass(class_name="Hip Hop Yoga", calorie_per_minute=1, length=30, intensity="Beginner")
class_list = {"kickboxing":kickboxing,"zumba":zumba, "hit":hit, "judo":judo, "dancing":dancing, "yoga":yoga}