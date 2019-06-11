<template>
  <div id="app">
    <h1>Menu</h1>
    <ul>
      <li><router-link to="/test_login">Test Login</router-link></li>
      <li><router-link to="/test_api">Test Api</router-link></li>
      <li><router-link to="/base">Template-Base</router-link></li>
    </ul>
    <router-view></router-view>
  </div>
</template>

<script>
// import api from './api/index.js'
export default {
  name: 'app',
  data () {
    return {

    }
  },
  methods:{

  },

}
</script>

<style>

</style>
