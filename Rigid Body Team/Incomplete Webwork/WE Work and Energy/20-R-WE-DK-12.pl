## DESCRIPTION
## 20-R-WE-DK-16 Lever system designed to fall slowly, find spring constant for specific ang. vel
## ENDDESCRIPTION

## KEYWORDS('kinetic energy','principle of work and energy','lever system','work','angular velocity','potential energy')
## DBsubject(Dynamics)
## DBchapter(Work and Energy)
## DBsection(Principle of Work and Energy)
## Date(2020-08-06)
## Author(David Kim)
## Institution(University of British Columbia)
## Level(Intermediate)
## RESOURCES('20-R-WE-16.png')

########################################################

DOCUMENT();

loadMacros(
	"PGstandard.pl",	# Standard macros for PG language
	"MathObjects.pl",
	"PGML.pl",
	"parserPopUp.pl",
	"parserMultiAnswer.pl",
    "parserRadioButtons.pl",
	"weightedGrader.pl",
	#"source.pl",			# allows code to be displayed on certain sites
	#"PGcourse.pl", 	 # Customization file for the course
);

#######################################################
#Setup


Context("Numeric");		# or Complex

#---------------Tolerance------------------#
Context()->flags->set(
tolerance=>.03,
tolType=>'relative');  #relative or absolute

#-------------- Image Scaling---------------#
$imgScale = 0.2;
	#aspect ratio


#---- Random variables for this problem --------#

$mrod = random(5,15,1);
$mmass = random(1,8,0.25);
$l = random(0.3,1.2,0.05);
$theta = random(45,60,1);
$thetarad = $theta*pi/180;
$angvel = random(0.5,1,0.1);

$theta0 = 30*pi/180;

#---- Formulas to compute answers --------------#

$I = 1/3*$mrod*$l**2;
$vel = sqrt(($angvel*$l*sin($thetarad))**2+($angvel*$l*cos($thetarad))**2);


$k = (-$mrod*9.81*($l*cos($thetarad)-$l*cos($theta0))-$mmass*9.81*($l*cos($thetarad)-$l*cos($theta0)) - 0.5*$I*$angvel**2-0.5*$mmass*$vel**2)/(0.5*($l*sin($thetarad)-$l*sin($theta0)**2));

########################################################;
#PGML

BEGIN_PGML	

[@ image( "20-R-KIN-WE-16.png", width=>[$width], height=>[$height]) @]*

A hardworking engineering student is designing a lever system that will slowly lower the lever and its load.
The [`[$mrod]`] [`kg`] slender rod BC has a mass [`m = `] [`[$mmass]`] [`kg`] attached at the rod's center of gravity G,
and a length [`l = `] [`[$l]`] [`m`]. If the rod is released from rest when the spring is unstretched at [`\theta = `] [`30`][`^{\circ}`],
determine the spring constant [`k`] needed to obtain an angular velocity of [`\omega = `] [`[$angvel]`] [`rad/s`] at the
instant [`\theta = `] [`[$theta]`][`^{\circ}`]. As the rod rotates, the spring always remains horizontal because of the roller support at A.

[`k = `] [____]{"$k"} [`N/m`]  


END_PGML

ENDDOCUMENT();