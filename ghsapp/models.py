from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
]

YES_NO_CHOICES = [
        ('Y', "Yes"),
        ('N', "No"),
]

class userInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=12)
    profile_pic = models.ImageField(
        upload_to='static/photos/', default='photos/default.png', null=True, blank=True)
    dob = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username


class doctorInfo(models.Model):

    

    DEGREE_CHOICES = [
        ("MBBS", "Bachelor of Medicine, Bachelor of Surgery(MBBS)"),
        ("BDS", "Bachelor of Dental Surgery(BDS)"),
        ("BAMS", "Bachelor of Ayurvedic Medicine and Surgery(BAMS)"),
        ("BUMS", "Bachelor of Unani Medicine and Surgery(BUMS)"),
        ("BHMS", "Bachelor of Homeopathy Medicine and Surgery(BHMS)"),
        ("BYNS", "Bachelor of Yoga and Naturopathy Sciences(BYNS)"),
        ("B.V.Sc & AH", "Bachelor of Veterinary Sciences and Animal Husbandry(BVSc&AH)"),
        ("MD", "Doctor of Medicine(MD)"),
        ("MS", "Master of Surgery(MS)"),
        ("DM", "Doctorate of Medicine(DM)"),
    ]

    SPECIALITIES_CHOICES = [
        ("ENT", "Ear, Nose and Throat"),
        ("GS", "General Surgery"),
        ("OP", "Ophthalmology"),
        ("OR", "Orthopaedics"),
        ("OAG", "Obstetrics and Gynaecology"),
        ("DVL", "Dermatology, Venerology and Leprosy"),
        ("AST", "Anaesthesiology"),
        ("PSY", "Psychiatry"),
        ("PTH", "Pathology"),
        ("SVD", "Skin and Venereal diseases"),
        ("PHRM", "Pharmacology"),
        ("PMR", "Physical Medicine and Rehabilitation"),
        ("PHY", "Physiology"),
        ("CRD", "Cardiology"),
        ("PDT", "Paediatrics"),
    ]

    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=12)
    profile_pic = models.ImageField(
        upload_to='static/photos/', default='photos/default.png', null=True, blank=True)
    hospital_name = models.CharField(max_length=70, blank=True)
    degree_type = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    specialities_type = models.CharField(
        max_length=50, choices=SPECIALITIES_CHOICES)
    dob = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.doctor.username


class History(models.Model):
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    date = models.DateField(auto_now=True)
    disease = models.CharField(max_length=200)
    medicine = models.TextField()
    charges = models.PositiveIntegerField()
    hospital_name = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return "{} has detected {} of {}".format(self.doctor.username, self.disease, self.user.username)


class Appointment(models.Model):
    doctor_app = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor_app')
    user_app = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_app')
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)

    def __str__(self):
        return "{} has appointmant of {} on {} at {}".format(self.user_app.username, self.doctor_app.username, self.date, self.time)

class Feedback(models.Model):

    doctor_feed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor_feed')
    user_feed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_feed')
    waiting_time = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    recommendation = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    feedback = models.TextField(blank=True)
