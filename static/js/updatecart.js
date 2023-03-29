
function getValues(object) {
    price = object.getAttribute('data-price');
    id = object.getAttribute('cartid');
    qnt = object.value;
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    var formData = new FormData();
        formData.append( 'qnt', parseInt(qnt));
        formData.append( 'price', parseFloat(price));
        formData.append( ' cid',parseInt(id));

  
    //let url = '/cart/updatecart?qnt=' + parseInt(qnt) + '&price='+ parseFloat(price) + '&cid=' + parseInt(id);
    let url ='/cart/updatecart/';

        fetch(url, {
            method: 'POST',
            mode: 'cors',   
            headers: {'Accept': 'application/json',
             'Content-Type': 'application/json', 
                 'X-CSRFToken': token },
            credentials : 'same-origin',
            body: JSON.stringify(formData)
        }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.')
            }
            else {
                console.log(response)
            }  
              
        }).catch(console.error)
}