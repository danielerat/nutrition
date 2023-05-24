class HEALTH_CALCULATOR:
    @staticmethod
    def calculate_bmi(height, weight):
        """Calculate Body Mass Index (BMI)"""
        body_mass = weight / (height ** 2)
        return body_mass

    @staticmethod
    def parse_bmi(body_mass):
        message=""
        if body_mass < 18.5:
            message = "Underweight"
        elif 18.5 <= body_mass < 24.9:
            message = "Normal weight"
        elif 24.9 <= body_mass < 29.9:
            message = "Overweight"
        else:
            message = "Obese"
        return {"body_mass":body_mass,"message":message}

    @staticmethod
    def calculate_body_fat_percentage(height, weight, gender):
        """Calculate Body Fat Percentage"""
        if gender == "male":
            body_fat_percentage = 1.20 * HEALTH_CALCULATOR.calculate_bmi(height, weight) + 0.23 * 25 - 16.2
        else:
            body_fat_percentage = 1.20 * HEALTH_CALCULATOR.calculate_bmi(height, weight) + 0.23 * 25 - 5.4
        return body_fat_percentage

    @staticmethod
    def calculate_basal_metabolic_rate(height, weight, age, gender):
        """Calculate Basal Metabolic Rate (BMR)"""
        if gender == "male":
            bmr = 10 * weight + 6.25 * (height * 100) - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * (height * 100) - 5 * age - 161
        return bmr

    @staticmethod
    def calculate_ideal_body_weight(height, gender, body_frame):
        """Calculate Ideal Body Weight"""
        if body_frame == "small":
            adjustment = 0.9
        elif body_frame == "large":
            adjustment = 1.1
        else:
            adjustment = 1.0

        if gender == "male":
            ideal_body_weight = (height * 100 - 100) - ((height * 100 - 100) * adjustment)
        else:
            ideal_body_weight = (height * 100 - 110) - ((height * 100 - 110) * adjustment)
        return ideal_body_weight

    @staticmethod
    def calculate_daily_caloric_intake(height, weight, age, gender, activity_level):
        """Calculate Daily Caloric Intake"""
        bmr = HEALTH_CALCULATOR.calculate_basal_metabolic_rate(height, weight, age, gender)

        if activity_level == "sedentary":
            daily_caloric_intake = bmr * 1.2
        elif activity_level == "light":
            daily_caloric_intake = bmr * 1.375
        elif activity_level == "moderate":
            daily_caloric_intake = bmr * 1.55
        elif activity_level == "active":
            daily_caloric_intake = bmr * 1.725
        else:
            daily_caloric_intake = bmr * 1.9

        return daily_caloric_intake
