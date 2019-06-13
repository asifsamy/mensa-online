<template>
    <div>
    <cheader></cheader>
    <cbanner></cbanner>
    <!-- Start component Area -->

    <!-- End component Area -->	
    <cfooter></cfooter>
    </div>
    	
</template>

<script>
// Import child components
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
