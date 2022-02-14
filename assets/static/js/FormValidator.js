var _phone , _fullname , _address , _email , _reservation;
var _item , _quantity, _price;
function formValidatorBuilder(phone,fullname,address,email,reservation) {
    _phone = phone;
    _fullname = fullname;
    _address = address;
    _email = email;
    _reservation = reservation;
    _item = document.getElementById("product").innerHTML;
    _quantity = document.getElementById("quantity").innerHTML;
    _price = document.getElementById("price").innerHTML;
    
        // do server sided code here

        var makeOrder = {
                            "phone":_phone,
                            "fullname":_fullname,
                            "address":_address,
                            "email":_email,
                            "item":_item,
                            "quantity":parseInt(_quantity),
                            "payment":parseInt(_price),
                            "reservationDate":_reservation
                        }
        alert("Thankyou for your order! kindly check your email for your order information")
        window.location.href = '/';
        jQuery.ajax({
            type : "POST",
            dataType:'json',
            url : '/api/orders',
            data : JSON.stringify(makeOrder),
            success: function() {
                alert("Thankyou for your order! kindly check your email for your order information");
                window.location.href = '/';
            }
        });   
        console.log(JSON.stringify(makeOrder)) // for debgging purpose
        
    
}
