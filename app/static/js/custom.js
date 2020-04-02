jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

window.onload = function(){
  try {
    var x = document.getElementById('123').getAttribute('value')
    console.log(x)
    if (x == "User") {
      hiddenDiv.style.display='inline-block';
      Form.fileURL.focus();
    }
    else {
      hiddenDiv.style.display='none';
    }
  }

  catch (err) {}

  finally {
    // Hide empty div cards on edit page
    var divs = document.getElementsByClassName("card mt-4");
    for (i = 0; i < divs.length; i++ ) {
      console.log(divs[i].getElementsByClassName("list-group list-group-flush"))
      if (divs[i].getElementsByClassName("list-group list-group-flush").length == 0) {
        divs[i].hidden = true;
      }
    }
  }
}

function show(aval) {
    if (aval == "User") {
      hiddenDiv.style.display='inline-block';
      Form.fileURL.focus();
    }
    else{
      hiddenDiv.style.display='none';
    }
  }

(function() {
  try {
    var password = document.getElementById('password');
    password.addEventListener('keypress', function(event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            document.getElementById('warnbtn').click();
        }
    });
  }
  catch (err) {}
}());
