var _name , _address, _tel , _email , _reservation;

function formValidatorBuilder(name,address,tel,email,reservation) {
    _name = document.getElementById(name);
    _address = document.getElementById(address);
    _tel = document.getElementById(tel);
    _email = document.getElementById(email);
    _reservation = document.getElementById(reservation);
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (_name.value.length == 0 || _address.value.length == 0 || _tel.value.length != 11 || _reservation.value.length == 0){
        alert("Can't proceed! All fields must have a valid inputs!");
        return false;
    }
     if (!_email.value.match(mailformat)){
        alert("Can't proceed! Your entered email is not valid!");
        return false;
    }
    else {
        window.location.href="order.html"
    }
}
