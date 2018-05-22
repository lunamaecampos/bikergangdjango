$('#tourselectform').submit(function(){
  console.log("hello");
  var artist = $("#artist").val();
  $("#tourselectform").attr('action','/tourartistselect/'+artist);
});
