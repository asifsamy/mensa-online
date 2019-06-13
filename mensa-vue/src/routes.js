// D1. Import the component from the components folder.
import test_login from './components/test_login.vue'
import test_api from './components/test_api.vue'
import base from './components/base.vue'

const routes = [
    // D2. Create the path object which will be used to call the component
    {path: '/test_login', component: test_login},
    {path:'/test_api', component: test_api},
    {path:'/base', component:base}
];

// D3. Export the routes as default. This will be used when Vue start to render the DOM.
export default routes;