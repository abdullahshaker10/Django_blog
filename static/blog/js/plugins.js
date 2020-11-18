// Dynamic Tabs
$(document).ready(function () {
    $('.dynamic-tabs-list li').on('click', function () {
        // console.log($(this).data('content'));
        $(this).addClass('active').siblings().removeClass('active');
        $('.dynamic-tabs-content > div').hide();
        $($(this).data('content')).fadeIn();
    });
});

$(document).ready(function () {
    $('.counter-count').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 1000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });
});

$(document).ready(function () {
    $('tr').each(function () {
        var totScore = 0;
        $(this).find('.subjects').each(function () {
            var marks = $(this).text();
            if(marks.length!==0)
            {
                totScore +=parseFloat(marks) * 1000;
            }
        });
        $(this).find('#totalscore').html(totScore)
    });
});

$(document).ready(function () {
    $('#points-table').each(function () {
        var var01 = 0;
        var var02 = 0;
        $(this).find('#totalscore').each(function () {
            var scores = $(this).text();
            var01 += parseFloat(scores);
            // console.log(var01)
        });
        $(this).find('.subjects').each(function () {
            var active = $(this).text();
            var02 += parseFloat(active);
            // console.log(var02)
        });

        $('#totalactions').html(var02)
        $('#grandtotalscore').html(var01)
    });
});

$(document).ready(function() {
    $('#totalpoints').html(jQuery("#grandtotalscore").html());
});


// $(document).ready(function () {
//     $("#createComment").click(function () {
//         var serializedData = $('#createCommentForm').serialize();
//         console.log(serializedData);
//     });
// });



// $(document).ready(function () {
//     var $myForm = $('.my-ajax-form'); // select form class
//     $myForm.submit(function (event) {
//         event.preventDefault();
//         var $formData = $myForm.serialize(); // get all data from form which will be submitted to database
//         var $thisURL = $myForm.attr('action') || window.location.href; // data-url is attribute in form
//         $.ajax({
//             method:'POST',
//             url: $thisURL,
//             data: $formData,
//             success: handleSuccess,
//             error: handleError,
//         });
//         function handleSuccess(data) {
//             console.log('success');
//             console.log(data.message);
//             $myForm[0].reset();
//         }
//         function handleError(ThrowError) {
//             console.log('error');
//             console.log(ThrowError);
//         }
//     });
// });






