const routes = [
  {
    path: '/', name: 'index', component: () => import('pages/LandingPage.vue')
  },
  {
    path: '/login', name: 'login',  component: () => import('pages/LoginPage.vue')
  },

  {
    path: '/admin',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
