function Validate(){
    
    if( document.Bioform10.FirstName.value == "")   //First Name Validation
    {
        alert( "Please Provide Your First Name!" );
        document.Bioform10.FirstName.focus();
        return false;
    }
    if( document.Bioform10.LastName.value == "")    //Last Name Validation
    {
        alert( "Please Provide Your Last Name!");
        document.Bioform10.LastName.focus();
        return false;
    }
    if( document.Bioform10.Birth.value == "")   //D.O.B Validation
    {
        alert( "Please Provide Your Date Of Birth!")
        document.Bioform10.Birth.focus();
        return false;
    }
    if( document.Bioform10.parent.value == "")  //Parent Name Validation
    {
        alert( "Please Provide A Parent/Guardian Name!")
        document.Bioform10.parent.focus();
        return false;
    }
    if( document.Bioform10.email.value == "")   //Email Validation
    {
        alert( "Please Provide Your Email!");
        document.Bioform10.email.focus() ;
        return false;
    }
    if( document.Bioform10.Address.value == "")     //Adress Validation
    {
        alert( "Please Provide Your House Address")
        document.Bioform10.Address.focus() ;
        return false;
    }
    if( document.Bioform10.state.value == "-1")     // validation for state of origin
    {
        alert("Please Provide Your State!");
        return false;
    }
    if( document.Bioform10.Lga.value == "-1")       //validation for LGA
    {
        alert("Please Provide Your LGA")
        return false;
    }
    if( document.Bioform10.phone.value == "" || isNaN(document.Bioform10.phone.value) || document.Bioform10.phone.value.length != 11 )
    {                                                                                               
        alert( "Please Provide A Valid Phone Number!"); //Phone No Validation
        document.Bioform10.phone.focus();
        return false;
    }
    if( document.Acaform.Primary.value == "-1")     //form 2 primary validation
    {
        alert( "Please Provide Your School Of Choice!")
        return false;
    }
    if( document.Acaform.Secondary.value == "-1")   //secondary validation
    {
        alert( "Please Provide Your College Of Choice!") 
        return false;
    }
    if( document.Acaform.Tertiary.value == "-1")    //Tertiary Validation
    {
        alert( "Please Provide Institution Of Choice!")
        return false;
    }
    if( document.Acaform.Course.value == "-1")      //Course Validation
    {
        alert("Please provide Course Of Your Choosing!")
        return false;
    }
    return(true);
}

function validateEmail()        //Email Validation Code
{
var emailID = document.Bioform10.email.value;
atpos = emailID.IndexOf("@");
dotpos = emailID.lastIndexOf(".")
if (atpos < 1 || (dotpos - atpos < 2))
{
   alert("Please Enter Correct Email ID")
    document.Bioform10.email.focus();
    return false;
} 
return( true );
}
