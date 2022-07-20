     if ($(".reg-form")) {
         var fname_is_valid = false, lname_is_valid = false, address_is_valid = false, email_is_valid = false,
             password_is_valid = false, idno_is_valid = false, phone_is_valid = false;
         $("#regFName").keyup(function () {
             if (validateText($("#regFName"), $("#regFNameError"))) {
                 fname_is_valid = true;
             } else {
                 fname_is_valid = false;
             }

         });

         $("#regLName").keyup(function () {
             if (validateText($("#regLName"), $("#regLNameError"))) {
                 lname_is_valid = true;
             } else {
                 lname_is_valid = false;
             }

         });

         $("#regAddress").keyup(function () {
                if (validateText($("#regAddress"), $("#regAddressError"))) {
                    address_is_valid = true;
                } else {
                    address_is_valid = false;
                }
        });
            $("#regPhone").keyup(function () {
                if (validateTel($("#regPhone"), $("#regPhoneError"))) {
                    phone_is_valid = true;
                } else {
                    phone_is_valid = false;
                }
        });
        $("#regEmail").keyup(function () {
            if (validateEmail($("#regEmail"), $("#regEmailError"))) {
                email_is_valid = true;
            } else {
                email_is_valid = false;
            }
            });


        $("#regPassword").keyup(function () {
            value = $("#regPassword").val()
            if (value.length > 5) {
                if (validateText($("#regPassword"), $("#regPasswordError"))) {
                    password_is_valid = true;
                } else {
                    password_is_valid = false;
                }
            }
            else{
                $("#regPasswordError").innerHTML = 'The password must be greater than 4 characters.';
                $("#regPasswordError").removeClass('hidden');
            }
        });
        $("#regConPassword").keyup(function () {
            if ($("#regPassword").val() != $("#regConPassword").val()) {
                $("#regPasswordError").html("Password mismatch.");
                $("#regPasswordError").removeClass("hidden");
                $("#regConPassword").addClass("border-red-700");
                $("#regPassword").addClass("border-red-700");
                $("#regPassword").removeClass("border-green-500");
                $("#regConPassword").removeClass("border-green-500");
            } else {
                $("#regPasswordError").hide();
                $("#regConPassword").removeClass("border-red-700");
                $("#regPassword").removeClass("border-red-700");
                $("#regPassword").addClass("border-green-500");
                $("#regConPassword").addClass("border-green-500");
                password_is_valid = true;
                ;
            }
        });
        $("#regBtn").click(function (e) {
            $(".reg-btn-text").hide();
            e.preventDefault();
            if (fname_is_valid == true && lname_is_valid == true && address_is_valid == true && email_is_valid == true && password_is_valid == true) {
                $('reg-form').submit()
            } else {
                $(".reg-error-alert").html("Fill in all the fields");
                showAlert($(".reg-error-alert"));
            }
        });
        }



