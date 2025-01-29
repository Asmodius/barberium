import { createRouter, createWebHistory } from 'vue-router'

import SetupView from '../views/SetupView.vue'
import ShowView from '../views/ShowView.vue'
import WeekView from '../views/WeekView.vue'
import LookView from '../views/LookView.vue'
import MusicView from '../views/MusicView.vue'

const DEF_REDIRECT = { name: 'setup' }

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/setup', name: 'setup', component: SetupView },
    { path: '/show', name: 'show', component: ShowView },
    { path: '/week', name: 'week', component: WeekView },
    { path: '/look', name: 'look', component: LookView },
    { path: '/musik', name: 'musik', component: MusicView },
    { path: '/:pathMatch(.*)', redirect: DEF_REDIRECT }
  ],
})

export default router
