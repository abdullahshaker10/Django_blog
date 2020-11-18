
let id = '{{post.id}}';
let url = '/api/post/'+id;
$( ".validate" ).click(function() {
    fetch(url, {
        method: 'GET',
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
      let inputCoupon = $(".coupon").val();
      let correctCoupon = data.coupon['code'];
      if (inputCoupon !== correctCoupon ){// coupon input is not correct
              $(".with_copoun").hide();
              $(".without_copoun").show();
              $(".right_coupon").remove();
              $(".coupon").css("border","2px solid red");
              if(!$(".wrong_coupon").length){
                   $(".coupon").parent().after("<div class=' wrong_coupon' style='color:red;margin-bottom: 20px;'>Ivalid Coupon</div>");
              }
             fetch(url, {
                headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                },
                method: 'PATCH',
                body: JSON.stringify({'state': false } )
                }).then((response)=>{
                 return response.json();
                 }).then((data)=>{
                    $('.finalPrice' ).append(data.final_price)
                    $('.finalPrice' ).replaceWith('<b> Final Price : </b>' +  data.final_price + '$')
                    $('.total' ).text('Total: ' +  data.final_price + '$')
                 })
        }
      else{ //coupon input is correct
        $(".without_copoun").hide();
        $(".with_copoun").show();
        $(".wrong_coupon").remove();
        $(".coupon").css("border","2px solid green");
        if(!$(".right_coupon").length){
            $(".coupon").parent().after("<div class='right_coupon' style='color:green;margin-bottom: 20px;'>Valid Coupon</div>");
        }
        fetch(url, {
            headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            method: 'PATCH',
            body: JSON.stringify({'state': true } )
            }).then((response)=>{
               return response.json();
            }).then((data)=>{
             $('.priceAfterDiscount' ).replaceWith('<b> Price After Discount : </b>' + data.get_total_price_after_discount + '$')
             $('.finalPrice' ).replaceWith('<b> Final Price : </b>' +  data.final_price + '$')
             $('.total' ).text('Total: ' +  data.final_price + '$')

               console.log(data)
            })
        }
    })
})
