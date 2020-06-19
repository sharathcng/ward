function GEEKFORGEEKS()                                    
{ 
    var name = document.forms["RegForm"]["name"];               
    var email = document.forms["RegForm"]["email"];    
    var userid = document.forms["RegForm"]["userid"];  
    var mobilenum =  document.forms["RegForm"]["mobilenum"];  
    var gender = document.forms["RegForm"]["gender"];  
    var profile_pic = document.forms["RegForm"]["profile_pic"];  
    var password = document.forms["RegForm"]["password"];  

    if (name.value == "")                                  
    { 
        window.alert("Please enter your name."); 
        name.focus(); 
        return false; 
    } 
   
    if (userid.value == "")                               
    { 
        window.alert("Please enter your userid."); 
        address.focus(); 
        return false; 
    } 
       
    if (email.value == "")                                   
    { 
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
   
    if (mobilenum.value == "")                           
    { 
        window.alert("Please enter your telephone number."); 
        phone.focus(); 
        return false; 
    } 
   
    if (password.value == "")                        
    { 
      var passw = /^[A-Za-z]\w{7,14}$/;
      if(inputtxt.value.match(passw)) 
      { 
      alert('Correct, try another...')
      return true;
      }
      else
      { 
      alert('Wrong...!')
      return false; 
    } 
   
    return true; 
}