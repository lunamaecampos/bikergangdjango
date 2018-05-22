var landingAnimation = function(){
  console.log('hello');
  $('.imagecolumns').find('#hero1').delay(10).animate({opacity:1, left:0},'400');
  $('#middlecolumn').find('#bikerlogo').delay(100).animate({opacity:1, left:0},'slow');
  $('#middlecolumn').find('.socialicon').delay(200).animate({opacity:1, left:0},'400');
  $('.imagecolumns').find('#hero2').delay(300).animate({opacity:1, left:60},'400');
  $('.imagecolumns').find('#hero3').delay(600).animate({opacity:1, left:0},'400');
  $('.imagecolumns2').find('#hero4').delay(700).animate({opacity:1, left:-60},'400');
  $('.imagecolumns2').find('#hero5').delay(1000).animate({opacity:1, left:0},'400');
  $('.imagecolumns2').find('#hero6').delay(1300).animate({opacity:1, left:-30},'400');
  console.log('oh why hello again')
}
$(document).ready(function(){
  landingAnimation();
});
