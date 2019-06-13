<template>
    <div>
    <cheader></cheader>
    <cbanner></cbanner>
    <!-- Start menu-area Area -->
    <section class="menu-area section-gap" id="menu">
        
        <div class="container">
			<div class="row d-flex justify-content-center">
				<div class="menu-content pb-70 col-lg-8">
					<div class="title text-center">
						<h1 class="mb-10">What kind of Foods we serve for you</h1>
					</div>
				</div>
			</div>	

            <ul class="filter-wrap filters col-lg-12 no-padding">
                <li class="active" data-filter="*">All Menu</li>
                <li data-filter=".Veg">Veg</li>
                <li data-filter=".Nonveg">Non-Veg</li>
				<li data-filter=".salads">Salads</li>
                <li data-filter=".desserts">Desserts</li>
                <li data-filter=".beverages">Beverages</li>					
            </ul>
           
            <div class="filters-content">
                <div class="row grid">
                    <div class="col-md-6 all Veg">
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>Cappuccion</h4>
								<h4 class="price">$49</h4>
							</div>			
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>		
							<h4 class="calorie">50 calories</h4>
						</div>					                               
                    </div>      
                    <div class="col-md-6 all Veg">						
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>Mocha</h4>
								<h4 class="price">$49</h4>
							</div>
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>			
                            <h4 class="calorie">50 calories</h4>									
						</div>
                    </div>		

                    <div class="col-md-6 all Nonveg">
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>Piccolo Latte</h4>
								<h4 class="price">$49</h4>
							</div>
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>	
							<h4 class="calorie">50 calories</h4>
						</div>
                    </div>		
					
					<div class="col-md-6 all salads">
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>mixed</h4>
								<h4 class="price">$49</h4>
							</div>			
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>
							<h4 class="calorie">50 calories</h4>
						</div>
                    </div>
					
                    <div class="col-md-6 all desserts">
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>Americano</h4>
								<h4 class="price">$49</h4>
							</div>			
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>
							<h4 class="calorie">50 calories</h4>
						</div>
                    </div>  
                    <div class="col-md-6 all beverages">
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>Ristretto</h4>
								<h4 class="price">$49</h4>
							</div>
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>			
							<h4 class="calorie">50 calories</h4>				
						</div>
                    </div>  
                     <div class="col-md-6 all beverages">
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>Macchiato</h4>
								<h4 class="price">$49</h4>
							</div>			
							<p>
								Usage of the Internet is becoming more common due to rapid advance.
							</p>		
							<h4 class="calorie">50 calories</h4>
						</div>
                    </div>							
                </div>
            </div>
            
        </div>
    </section>
    <!-- End menu-area Area -->		
    <cfooter></cfooter>
    </div>
    
</template>

<script>
// Import components
import header from './common/header.vue'
import banner from './common/banner.vue'
import footer from './common/footer.vue'

export default {
components:{
    'cheader':header,
    'cbanner':banner,
    'cfooter':footer,
  },
}
</script>

<style>

</style>
