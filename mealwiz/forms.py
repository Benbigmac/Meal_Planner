from .dbhandler import mealWizDB
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField, DecimalField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Optional


class addFood(FlaskForm):
    foodname = StringField('Food Name', validators=[DataRequired()])

    servingsize = FloatField(
        "Serving Size",
        validators=[InputRequired(), NumberRange(min=0)]
    )
    servingsizeunit = SelectField(
        "Serving Size Unit",
        validators=[DataRequired()],choices=[('Grams','g'),("Milliliters",'ml'),('Cups','C')],
        description="Unit of measurement for serving size (e.g., grams, cups)."
    )
    carbs = DecimalField('Carbohydrates (g)', places=2, validators=[DataRequired()])
    protein = DecimalField('Protein (g)', places=2, validators=[DataRequired()])
    fat = DecimalField('Fat (g)', places=2, validators=[DataRequired()])
    #missing serving size and units

    fiber = DecimalField('Fiber (g)', places=2, validators=[Optional()])
    saturated_fat = DecimalField('Saturated Fat (g)', places=2, validators=[Optional()])
    trans_fat = DecimalField('Trans Fat (g)', places=2, validators=[Optional()])
    cholesterol = DecimalField('Cholesterol (mg)', places=2, validators=[Optional()])
    sodium = DecimalField('Sodium (mg)', places=2, validators=[Optional()])
    potassium = DecimalField('Potassium (mg)', places=2, validators=[Optional()])
    calcium = DecimalField('Calcium (mg)', places=2, validators=[Optional()])
    iron = DecimalField('Iron (mg)', places=2, validators=[Optional()])

    vitamin_a = DecimalField('Vitamin A (mg)', places=2, validators=[Optional()])
    vitamin_c = DecimalField('Vitamin C (mg)', places=2, validators=[Optional()])
    vitamin_d = DecimalField('Vitamin D (mg)', places=2, validators=[Optional()])
    vitamin_k = DecimalField('Vitamin K (mg)', places=2, validators=[Optional()])

    magnesium = DecimalField('Magnesium (mg)', places=2, validators=[Optional()])
    zinc = DecimalField('Zinc (mg)', places=2, validators=[Optional()])

    glycemic_index = DecimalField('Glycemic Index', places=2, validators=[Optional()])
    glycemic_load = DecimalField('Glycemic Load', places=2, validators=[Optional()])

    omega_3 = DecimalField('Omega-3 Fatty Acids (g)', places=2, validators=[Optional()])
    omega_6 = DecimalField('Omega-6 Fatty Acids (g)', places=2, validators=[Optional()])

    FoodType = SelectField("Food Category", choices=[])
    submit = SubmitField('Submit')

class addRatio(FlaskForm):
        ratioName = StringField('Ratio Name', validators=[DataRequired()])
        ratioTime = StringField('Ratio Name', validators=[DataRequired()])
        CarbRatio = FloatField(
            "Carb Ratio",
            validators=[InputRequired(), NumberRange(min=0)]
        )
        ProteinRatio = FloatField(
            "Protein Ratio",
            validators=[InputRequired(), NumberRange(min=0)]
        )
        FatRatio = FloatField(
            "Fat Ratio",
            validators=[InputRequired(), NumberRange(min=0)]
        )
