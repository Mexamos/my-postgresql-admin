import Vue from 'vue'
import VueRouter from 'vue-router'
import Databases from '../views/Databases.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'databases',
    component: Databases
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
