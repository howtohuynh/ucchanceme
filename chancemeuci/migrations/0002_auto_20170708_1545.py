# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chancemeuci', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='uc_gpa',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='ethnicity',
            field=models.CharField(choices=[('American Indian / Alaskan Native', 'American Indian / Alaskan Native'), ('Asian / Pacific Islander', 'Asian / Pacific Islander'), ('Black, non - Hispanic', 'Black, non - Hispanic'), ('Hispanic', 'Hispanic'), ('White, non - Hispanic', 'White, non - Hispanic'), ('Unknown / declined to state', 'Unknown / declined to state'), ('International student', 'International student')], max_length=128),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Not stated', 'Not stated')], max_length=128),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='high_school',
            field=models.CharField(choices=[('ABRAHAM LINCOLN SR HIGH SCHOOL', 'ABRAHAM LINCOLN SR HIGH SCHOOL'), ('ALAMEDA HIGH SCHOOL', 'ALAMEDA HIGH SCHOOL'), ('ALHAMBRA HIGH SCHOOL', 'ALHAMBRA HIGH SCHOOL'), ('ALISO NIGUEL HIGH SCHOOL', 'ALISO NIGUEL HIGH SCHOOL'), ('ARCADIA SENIOR HIGH SCHOOL', 'ARCADIA SENIOR HIGH SCHOOL'), ('ARNOLD O BECKMAN HIGH SCHOOL', 'ARNOLD O BECKMAN HIGH SCHOOL'), ('ARROYO HIGH SCHOOL', 'ARROYO HIGH SCHOOL'), ('BISHOP MONTGOMERY HIGH SCHOOL', 'BISHOP MONTGOMERY HIGH SCHOOL'), ('BOLSA GRANDE HIGH SCHOOL', 'BOLSA GRANDE HIGH SCHOOL'), ('BREA-OLINDA HIGH SCHOOL', 'BREA-OLINDA HIGH SCHOOL'), ('BURBANK SR HIGH SCHOOL', 'BURBANK SR HIGH SCHOOL'), ('CALIFORNIA ACADEMY MATH & SCIENCE', 'CALIFORNIA ACADEMY MATH & SCIENCE'), ('CANYON HIGH SCHOOL', 'CANYON HIGH SCHOOL'), ('CAPISTRANO VALLEY HIGH SCHOOL', 'CAPISTRANO VALLEY HIGH SCHOOL'), ('CASTRO VALLEY HIGH SCHOOL', 'CASTRO VALLEY HIGH SCHOOL'), ('CENTENNIAL HIGH SCHOOL', 'CENTENNIAL HIGH SCHOOL'), ('CERRITOS HIGH SCHOOL', 'CERRITOS HIGH SCHOOL'), ('CHINO HILLS HIGH SCHOOL', 'CHINO HILLS HIGH SCHOOL'), ('CRESCENTA VALLEY HIGH SCHOOL', 'CRESCENTA VALLEY HIGH SCHOOL'), ('CYPRESS HIGH SCHOOL', 'CYPRESS HIGH SCHOOL'), ('DIAMOND BAR HIGH SCHOOL', 'DIAMOND BAR HIGH SCHOOL'), ('DIAMOND RANCH HIGH SCHOOL', 'DIAMOND RANCH HIGH SCHOOL'), ('DOWNEY HIGH SCHOOL', 'DOWNEY HIGH SCHOOL'), ('EDISON HIGH SCHOOL', 'EDISON HIGH SCHOOL'), ('EL CAMINO REAL SR HIGH SCHOOL', 'EL CAMINO REAL SR HIGH SCHOOL'), ('EL TORO HIGH SCHOOL', 'EL TORO HIGH SCHOOL'), ('ELEANOR ROOSEVELT HIGH SCHOOL', 'ELEANOR ROOSEVELT HIGH SCHOOL'), ('ESPERANZA HIGH SCHOOL', 'ESPERANZA HIGH SCHOOL'), ('EVERGREEN VALLEY HIGH SCHOOL', 'EVERGREEN VALLEY HIGH SCHOOL'), ('FAIRMONT PREPARATORY ACADEMY', 'FAIRMONT PREPARATORY ACADEMY'), ('FOUNTAIN VALLEY HIGH SCHOOL', 'FOUNTAIN VALLEY HIGH SCHOOL'), ('FRANCISCO BRAVO MEDICAL MAGNET CENTER', 'FRANCISCO BRAVO MEDICAL MAGNET CENTER'), ('GABRIELINO HIGH SCHOOL', 'GABRIELINO HIGH SCHOOL'), ('GALILEO HIGH SCHOOL', 'GALILEO HIGH SCHOOL'), ('GARDEN GROVE HIGH SCHOOL', 'GARDEN GROVE HIGH SCHOOL'), ('GEORGE WASHINGTON HIGH SCHOOL', 'GEORGE WASHINGTON HIGH SCHOOL'), ('GLEN A. WILSON HIGH SCHOOL', 'GLEN A. WILSON HIGH SCHOOL'), ('GLENDALE SENIOR HIGH SCHOOL', 'GLENDALE SENIOR HIGH SCHOOL'), ('GRANADA HILLS HIGH SCHOOL', 'GRANADA HILLS HIGH SCHOOL'), ('GRETCHEN WHITNEY HIGH SCHOOL', 'GRETCHEN WHITNEY HIGH SCHOOL'), ('GROVER CLEVELAND HIGH SCH. (HUMAN. MAG.)', 'GROVER CLEVELAND HIGH SCH. (HUMAN. MAG.)'), ('HECTOR GODINEZ FUNDAMENTAL HS', 'HECTOR GODINEZ FUNDAMENTAL HS'), ('HOMESTEAD HIGH SCHOOL', 'HOMESTEAD HIGH SCHOOL'), ('HUNTINGTON BEACH HIGH SCHOOL', 'HUNTINGTON BEACH HIGH SCHOOL'), ('IRVINE HIGH SCHOOL', 'IRVINE HIGH SCHOOL'), ('IRVINGTON HIGH SCHOOL', 'IRVINGTON HIGH SCHOOL'), ('JOHN A. ROWLAND HIGH SCHOOL', 'JOHN A. ROWLAND HIGH SCHOOL'), ('JOHN F. KENNEDY HIGH SCHOOL', 'JOHN F. KENNEDY HIGH SCHOOL'), ('JOHN MARSHALL SR HIGH SCHOOL', 'JOHN MARSHALL SR HIGH SCHOOL'), ('LA QUINTA HIGH SCHOOL', 'LA QUINTA HIGH SCHOOL'), ('LAKEWOOD SENIOR HIGH SCHOOL', 'LAKEWOOD SENIOR HIGH SCHOOL'), ('LOARA HIGH SCHOOL', 'LOARA HIGH SCHOOL'), ('LONG BEACH POLYTECHNIC HIGH SCHOOL', 'LONG BEACH POLYTECHNIC HIGH SCHOOL'), ('LOS ALAMITOS HIGH SCHOOL', 'LOS ALAMITOS HIGH SCHOOL'), ('LOS AMIGOS HIGH SCHOOL', 'LOS AMIGOS HIGH SCHOOL'), ('LOS OSOS', 'LOS OSOS'), ('LOWELL HIGH SCHOOL', 'LOWELL HIGH SCHOOL'), ('LYNBROOK HIGH SCHOOL', 'LYNBROOK HIGH SCHOOL'), ('MARINA HIGH SCHOOL', 'MARINA HIGH SCHOOL'), ('MARK KEPPEL HIGH SCHOOL', 'MARK KEPPEL HIGH SCHOOL'), ('MATER DEI HIGH SCHOOL', 'MATER DEI HIGH SCHOOL'), ('MILPITAS HIGH SCHOOL', 'MILPITAS HIGH SCHOOL'), ('MISSION SAN JOSE HIGH SCHOOL', 'MISSION SAN JOSE HIGH SCHOOL'), ('MONTA VISTA HIGH SCHOOL', 'MONTA VISTA HIGH SCHOOL'), ('MONTCLAIR HIGH SCHOOL', 'MONTCLAIR HIGH SCHOOL'), ('NORTH HIGH SCHOOL', 'NORTH HIGH SCHOOL'), ('NORTHWOOD HIGH SCHOOL', 'NORTHWOOD HIGH SCHOOL'), ('ORANGE HIGH SCHOOL', 'ORANGE HIGH SCHOOL'), ('OTAY RANCH HIGH SCHOOL', 'OTAY RANCH HIGH SCHOOL'), ('OXFORD ACADEMY', 'OXFORD ACADEMY'), ('PACIFICA HIGH SCHOOL', 'PACIFICA HIGH SCHOOL'), ('PALOS VERDES PENINSULA HIGH SCHOOL', 'PALOS VERDES PENINSULA HIGH SCHOOL'), ('PARAMOUNT HIGH SCHOOL', 'PARAMOUNT HIGH SCHOOL'), ('PIEDMONT HILLS HIGH SCHOOL', 'PIEDMONT HILLS HIGH SCHOOL'), ('RANCHO ALAMITOS HIGH SCHOOL', 'RANCHO ALAMITOS HIGH SCHOOL'), ('RANCHO BERNARDO HIGH SCHOOL', 'RANCHO BERNARDO HIGH SCHOOL'), ('RANCHO CUCAMONGA HIGH SCHOOL', 'RANCHO CUCAMONGA HIGH SCHOOL'), ('RICHARD GAHR HIGH SCHOOL', 'RICHARD GAHR HIGH SCHOOL'), ('ROSEMEAD HIGH SCHOOL', 'ROSEMEAD HIGH SCHOOL'), ('RUBEN AYALA HIGH SCHOOL', 'RUBEN AYALA HIGH SCHOOL'), ('SAN GABRIEL HIGH SCHOOL', 'SAN GABRIEL HIGH SCHOOL'), ('SAN MARINO HIGH SCHOOL', 'SAN MARINO HIGH SCHOOL'), ('SANTIAGO HIGH SCHOOL', 'SANTIAGO HIGH SCHOOL'), ('SANTIAGO HIGH SCHOOL', 'SANTIAGO HIGH SCHOOL'), ('SCRIPPS RANCH HIGH SCHOOL', 'SCRIPPS RANCH HIGH SCHOOL'), ('SEGERSTROM HIGH SCHOOL', 'SEGERSTROM HIGH SCHOOL'), ('SOUTH GATE SR HIGH SCHOOL', 'SOUTH GATE SR HIGH SCHOOL'), ('SOUTH HIGH SCHOOL', 'SOUTH HIGH SCHOOL'), ('STOCKDALE HIGH SCHOOL', 'STOCKDALE HIGH SCHOOL'), ('SUNNY HILLS HIGH SCHOOL', 'SUNNY HILLS HIGH SCHOOL'), ('TEMPLE CITY HIGH SCHOOL', 'TEMPLE CITY HIGH SCHOOL'), ('TESORO HIGH SCHOOL', 'TESORO HIGH SCHOOL'), ('TORRANCE HIGH SCHOOL', 'TORRANCE HIGH SCHOOL'), ('TORREY PINES HIGH SCHOOL', 'TORREY PINES HIGH SCHOOL'), ('TRABUCO HILLS HIGH SCHOOL', 'TRABUCO HILLS HIGH SCHOOL'), ('TROY HIGH SCHOOL', 'TROY HIGH SCHOOL'), ('UNIVERSITY HIGH SCHOOL', 'UNIVERSITY HIGH SCHOOL'), ('VALENCIA HIGH SCHOOL', 'VALENCIA HIGH SCHOOL'), ('VILLA PARK HIGH SCHOOL', 'VILLA PARK HIGH SCHOOL'), ('WALNUT HIGH SCHOOL', 'WALNUT HIGH SCHOOL'), ('WARREN HIGH SCHOOL', 'WARREN HIGH SCHOOL'), ('WEST COVINA HIGH SCHOOL', 'WEST COVINA HIGH SCHOOL'), ('WEST HIGH SCHOOL', 'WEST HIGH SCHOOL'), ('WESTMINSTER HIGH SCHOOL', 'WESTMINSTER HIGH SCHOOL'), ('WESTVIEW', 'WESTVIEW'), ('WOODBRIDGE HIGH SCHOOL', 'WOODBRIDGE HIGH SCHOOL'), ('WOODROW WILSON HIGH SCHOOL', 'WOODROW WILSON HIGH SCHOOL'), ('OTHER/NOT LISTED', 'OTHER/NOT LISTED')], max_length=128),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='major',
            field=models.CharField(choices=[('Art', 'Art'), ('Dance', 'Dance'), ('Drama', 'Drama'), ('Music - Performance', 'Music - Performance'), ('Music', 'Music'), ('Studio Art', 'Studio Art'), ('Undeclared', 'Undeclared'), ('Biological Sciences', 'Biological Sciences'), ('Biology/Education', 'Biology/Education'), ('Ecology and Evolutionary Biology', 'Ecology and Evolutionary Biology'), ('Business Administration', 'Business Administration'), ('Education Sciences', 'Education Sciences'), ('Aerospace Engineering', 'Aerospace Engineering'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Biomedical Engineering: Premed', 'Biomedical Engineering: Premed'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Environmental Engineering', 'Environmental Engineering'), ('Materials Science Engineering', 'Materials Science Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Undeclared', 'Undeclared'), ('Art History', 'Art History'), ('Chinese Language and Literature', 'Chinese Language and Literature'), ('Chinese Studies', 'Chinese Studies'), ('Comparative Literature', 'Comparative Literature'), ('English', 'English'), ('European Studies', 'European Studies'), ('Film and Media Studies', 'Film and Media Studies'), ('French', 'French'), ('Global Cultures', 'Global Cultures'), ('History', 'History'), ('Japanese Lanuage and Literature', 'Japanese Lanuage and Literature'), ('Korean Literature and Culture', 'Korean Literature and Culture'), ('Literary Journalism', 'Literary Journalism'), ('Philosophy', 'Philosophy'), ('Spanish', 'Spanish'), ('Undeclared', 'Undeclared'), ('Biomedical Computing', 'Biomedical Computing'), ('Business Information Management', 'Business Information Management'), ('Computer Game Science', 'Computer Game Science'), ('Computer Science', 'Computer Science'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Data Science', 'Data Science'), ('Informatics', 'Informatics'), ('Information and Computer Science', 'Information and Computer Science'), ('Software Engineering', 'Software Engineering'), ('Undeclared', 'Undeclared'), ('Nursing Science', 'Nursing Science'), ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'), ('Applied Physics', 'Applied Physics'), ('Chemistry', 'Chemistry'), ('Earth and Environmental Sciences', 'Earth and Environmental Sciences'), ('Earth and Environmental Studies', 'Earth and Environmental Studies'), ('Earth System Science', 'Earth System Science'), ('Environmental Science', 'Environmental Science'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Undeclared', 'Undeclared'), ('Public Health Policy', 'Public Health Policy'), ('Public Health Sciences', 'Public Health Sciences'), ('Criminology, Law and Society', 'Criminology, Law and Society'), ('Psychology and Social Behavior', 'Psychology and Social Behavior'), ('Social Ecology', 'Social Ecology'), ('Undeclared', 'Undeclared'), ('Urban Studies', 'Urban Studies'), ('Anthropology', 'Anthropology'), ('Business Economics', 'Business Economics'), ('Cognitive Sciences', 'Cognitive Sciences'), ('Economics', 'Economics'), ('International Studies', 'International Studies'), ('Political Science', 'Political Science'), ('Psychology ', 'Psychology '), ('Quantitative Economics', 'Quantitative Economics'), ('Social Policy and Public Service', 'Social Policy and Public Service'), ('Social Science', 'Social Science'), ('Sociology', 'Sociology'), ('Undeclared', 'Undeclared'), ('Undeclared', 'Undeclared')], max_length=128),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='residency',
            field=models.CharField(choices=[('California resident', 'California resident'), ('Other U.S. citizens or permanent residents', 'Other U.S. citizens or permanent residents'), ('International students', 'International students')], max_length=128),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='school',
            field=models.CharField(choices=[('Arts', 'Arts'), ('Biological Sciences', 'Biological Sciences'), ('Business', 'Business'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('Humanities', 'Humanities'), ('Info and Computer Sci', 'Info and Computer Sci'), ('Nursing Sciences', 'Nursing Sciences'), ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'), ('Physical Sciences', 'Physical Sciences'), ('Public Health', 'Public Health'), ('Social Ecology', 'Social Ecology'), ('Social Sciences', 'Social Sciences'), ('Undergrad Education', 'Undergrad Education')], max_length=128),
        ),
    ]