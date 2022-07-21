     if ($(".officer-form")) {

         var fname_is_valid = false, lname_is_valid = false, address_is_valid = false, email_is_valid = false,
             password_is_valid = false, phone_is_valid = false;

         $("#OFName").keyup(function () {
             if (validateText($("#OFName"), $("#OFNameError"))) {
                 fname_is_valid = true;
             } else {
                 fname_is_valid = false;
             }

         });

         $("#OLName").keyup(function () {
             if (validateText($("#OLName"), $("#OLNameError"))) {
                 lname_is_valid = true;
             } else {
                 lname_is_valid = false;
             }

         });

         $("#OAddress").keyup(function () {
                if (validateText($("#OAddress"), $("#OAddressError"))) {
                    address_is_valid = true;
                } else {
                    address_is_valid = false;
                }
        });
            $("#OPhone").keyup(function () {
                if (validateTel($("#OPhone"), $("#OPhoneError"))) {
                    phone_is_valid = true;
                } else {
                    phone_is_valid = false;
                }
        });
        $("#OEmail").keyup(function () {
            if (validateEmail($("#OEmail"), $("#OEmailError"))) {
                email_is_valid = true;
            } else {
                email_is_valid = false;
            }
            });


        $("#OPassword").keyup(function () {
            value = $("#OPassword").val()
            if (value.length > 5) {
                if (validateText($("#OPassword"), $("#OPasswordError"))) {
                    password_is_valid = true;
                } else {
                    password_is_valid = false;
                }
            }
            else{
                $("#OPasswordError").innerHTML = 'The password must be greater than 4 characters.';
                $("#OPasswordError").removeClass('hidden');
            }
        });
        $("#regConPassword").keyup(function () {
            if ($("#OPassword").val() != $("#OPasswordError").val()) {
                $("#OPasswordError").html("Password mismatch.");
                $("#OPasswordError").removeClass("hidden");
                $("#OConPassword").addClass("border-red-700");
                $("#OPassword").addClass("border-red-700");
                $("#OPassword").removeClass("border-green-500");
                $("#0ConPassword").removeClass("border-green-500");
            } else {
                $("#OPasswordError").hide();
                $("#0ConPassword").removeClass("border-red-700");
                $("#OPassword").removeClass("border-red-700");
                $("#OPassword").addClass("border-green-500");
                $("#OConPassword").addClass("border-green-500");
                password_is_valid = true;
                ;
            }
        });
        $("#OBtn").click(function (e) {
            $(".reg-btn-text").hide();
            e.preventDefault();
            if (fname_is_valid == true && lname_is_valid == true && address_is_valid == true && email_is_valid == true && password_is_valid == true) {
                $('officer-form').submit()
            } else {
                $(".reg-error-alert").html("Fill in all the fields");
                showAlert($(".reg-error-alert"));
            }
        });
        }



