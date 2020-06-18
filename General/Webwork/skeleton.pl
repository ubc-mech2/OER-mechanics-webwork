##DESCRIPTION
## This is where the description goes for the problem
##ENDDESCRIPTION

## DBsubject(SUBJECT)
## DBchapter(CHAPTER)
## DBsection(SECTION)
## Institution(University of British Columbia)
## Author(YOUR NAME)
## Date(DATE)
## Level(Intermediate)
## KEYWORDS('KEYWORDS','SAMPLE','TEST','ILOVEWEBWORK')
## RESOURCES('IMAGENAME.PNG')

##############################################################

DOCUMENT();

loadMacros(   
	"PGstandard.pl",     # Standard macros for PG language
	"MathObjects.pl",
	"PGML.pl",
	"parserPopUp.pl",
	"parserMultiAnswer.pl",
	"parserRadioButtons.pl",
	#"source.pl",        # allows code to be displayed on certain sites.
	#"PGcourse.pl", 	 # Customization file for the course
   	);

##############################################################
#
#  Setup
#
#

Context("Numeric");         # or Complex
#given
$dt = random(5,10,0.2);     # (lower, upper, stepsize)


#image scale
$imgScale = .2;

#image aspect ratio
$width = $imgScale*1847;
$height = $imgScale*1981;

#computation
$R_G = 50 - $h_G;



#set tolerance
Context()->flags->set(
tolerance=>.001,
tolType=>'absolute');  #absolute or relative

##############################################################
#
#  PGML 
#
#

BEGIN_PGML

[@ image( "imagename.png", width=>[$width], height=>[$height]) @]*

The mass center of a scooter rider is at [`[$h_G]`] [`m`] above the ground, and has a velocity of [`6`] [`m/s`] at that top of the hill (point [`A`]). [`[$dt]`] sec later the scooter rider reaches at the bottom of the hill (point [`B`]) and has a velocity of [`8`] [`m/s`]. The radius of curvature of the road is [`R = 50`] [`m`] at point [`B`].  
1. Calculate the angular velocity of the scooter rider when she reaches the bottom of the hill.  
2. Calculate the average angular velocity of the scooter rider during this ride (from point [`A`] to point [`B`]). 


[`\omega_B=`][___]{"$omega_B"} [`rad/s`]  
[`\omega_{ave}=`][___]{"$omega_av"} [`rad/s`]

_Round your answers to three decimal places_.

END_PGML

##############################################################

ENDDOCUMENT()];     #save as .pg