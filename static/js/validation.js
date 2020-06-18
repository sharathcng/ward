function validateForm() {
    var x = document.forms["myForm"]["userid"].value;
    if (x == "sharuhg") {
      alert("Name must be filled out");
      return false;
    }
  }