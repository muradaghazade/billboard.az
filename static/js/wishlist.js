ids = JSON.parse(localStorage.getItem('products'))
    
    data = {
        ids:ids
    }

    fetch('/api/products/', {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      })
        .then((resp) => resp.json())
        .then((data) => {
          price = 0
          console.log(data);
          data.forEach(element => {
            document.getElementById('tt-product-listing').innerHTML += 
            `
            <li class="col-6 col-md-4 col-lg-3 tt-col-item">
                    <div class="tt-product-02">
                      <div class="tt-image-box">
                        <a
                          class="image-link"
                          href="${element.image}"
                        >
                          <img
                            class="announce-img"
                            src="${element.image}"
                            alt=""
                          />
                        </a>
                        <div class="top-left">
                        </div>
                        <strong style="position:absolute; bottom:1px; right:10px;color:white;" class="code">Kod: ${element.code}</strong>
      
                      </div>
                      <div class="tt-wrapper-description">
                        <div class="tt-row-01">
                          <div class="tt-box-title">
                            <h2 class="tt-title address text-left">
                              ${element.title}
                            </h2>
                            <div class="category" style="display: none">T679</div>
                            <div
                              class="row text-left announce_info-row"
                              style="margin: 0px"
                            >
                              <div class="col-xs-6">
                                <i class="fas fa-sign"></i> ${element.category.title}<br />
                                <i class="fas fa-tags"></i> ${element.price} AZN
                              </div>
                              <div class="col-xs-6">
                                <i class="fas fa-ruler"></i>${element.size}sm<br />
                                <i class="fas fa-print"></i> ${element.support_price} AZN
                              </div>
                            </div>
                            <div
                              class="row text-left d-flex justify-content-between mt-2"
                              style="margin: 5px 0px 0px 0px"
                            >
                              <button
                              id="${element.id}"
                                type="button"
                                class="btn btn-secondary add_cart"
                              >
                              <i class="far fa-heart" id="${element.id}"></i>
                              <!-- <i style="color:#dd3d53;" class="fas fa-heart"></i> -->
                              </button>
                              <button
                                type="button"
                                class="btn btn-secondary"
                                style="width: 30% !important;"
                              >
                                <!-- <i class="fas fa-map-marker-alt"></i> -->
                                <img style="width:20px;height:20px;" src="/static/images/google-maps.png"/>
                              </button>
                              <button
                                type="button"
                                class="btn btn-secondary"
                                style="width: 30% !important;"
                                onclick="window.open('https://wa.me/994552132310?text=Kod:%20AB%20010', '_blank')"
                              >
                                <!-- <i class="fab fa-whatsapp"></i> -->
                                <img style="width:20px;height:20px;" src="/static/images/whatsapp.png" alt="">
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </li>
            `
          });
          
        })