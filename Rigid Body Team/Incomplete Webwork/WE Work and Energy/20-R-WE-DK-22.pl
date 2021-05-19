## DESCRIPTION
## 20-R-WE-DK-22 Slide box vs roll cylinder up a hill, find the work done by various forces
## ENDDESCRIPTION

## KEYWORDS('rolling','cylinder','angular velocity','moment','work','kinetics')
## DBsubject(Dynamics)
## DBchapter(Work and Energy)
## DBsection(Work)
## Date(2020-08-06)
## Author(David Kim)
## Institution(University of British Columbia)
## Level(Intermediate)
## RESOURCES('20-R-WE-22.png')

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
$theta = random(10,45,5);
$thetarad = $thetarad/180*pi;
$h = random(0.3,0.5,0.05);
$m = 5;
$mus = random(0.2,0.4,0.1);
$muk = $mus - 0.1;
$F = random(30,50,5);
$d = random(1,3,0.1);

#---- Formulas to compute answers --------------#
$boxUN = 0;


########################################################;
#PGML

BEGIN_PGML	

[@ image( "20-R-KIN-WE-9.png", width=>[$width], height=>[$height]) @]*

Montana James is shooting a scene in which he is running away from a foam cylinder (it will be replaced by a boulder in post-production).
If the cylinder has mass [`m = `] [`[$m]`] [`kg`] and a radius of [`r = `] [`[$r]`] [`m`], calculate the cylinders total kinetic energy.
Assume the cylinder rolls without slipping at an angular velocity of [`\omega = `] [`[$angvel]`] [`rad/s`].

[`T = `] [____]{"$U"} [`J`]    

END_PGML

ENDDOCUMENT();