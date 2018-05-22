var contentFadeIn = function(){
  $('#contentwrapper').delay(100).animate({opacity:1},'slow');
}
$(document).ready(function(){
  contentFadeIn();
});



// $(document).ready(function(){
//   $('#menuicon').click(function(){
//     $('#menubar').toggle();
//   });
// });

// $(document).ready(function(){
//   if (toggleFlag == false || toggleFlag == null){
//     $('#menuicon').click(function(){
//       console.log('left');
//       $('#contentwrapper').delay(10).animate({left:250}, 'fast');
//       toggleFlag = true;
//     });
//   } else {
//     $('#menuicon').click(function(){
//       $('#contentwrapper').animate({right:250}, 'fast');
//       console.log('right');
//       toggleFlag = false;
//     });
//   }
// });

$(document).ready(function(){
  var toggleFlag;
  $('#menuicon').click(function(){
    if (toggleFlag == false || toggleFlag == null){
      // $('#mobilebar').delay(10).animate({left:250}, 'fast');
      // $('#menubar').delay(10).attr('left', '-225px;');
      $('#menubar').delay(10).animate({left:-225}, '400');
      toggleFlag = true;
      console.log('left');
    } else {
      // $('#mobilebar').delay(10).animate({left:0}, 'fast');
      $('#menubar').delay(10).animate({left:-550}, '400');
      toggleFlag = false;
      console.log('right');
    }
  });
});
