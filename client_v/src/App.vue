<template>
  <div id="main">
    <ul>
      <li>
        <IconSetup />
      </li>
      <li class="active">
        <IconSmilePlus />
      </li>
      <li>
        <IconEvent />
      </li>
      <li>
        <IconArOnYou />
      </li>
      <li>
        <IconMusic />
      </li>
    </ul>

    <RouterView />
  </div>
  <!-- <header> -->
    <!-- <div class="wrapper"> -->
      <!-- <HelloWorld msg="You did it!" /> -->

      <!-- <nav> -->
        <!-- <RouterLink to="/">Home</RouterLink> -->
        <!-- <RouterLink to="/about">About</RouterLink> -->
      <!-- </nav> -->
    <!-- </div> -->
  <!-- </header> -->
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'

import IconSetup from './components/icons/IconSetup.vue'
import IconSmilePlus from './components/icons/IconSmilePlus.vue'
import IconArOnYou from './components/icons/IconArOnYou.vue'
import IconEvent from './components/icons/IconEvent.vue'
import IconMusic from './components/icons/IconMusic.vue'

</script>

<style scoped>
#main {
  display: flex;
  height: 100vh;
  /* background-color: burlywood; */
}

ul {
  /* width: 100px; */
  /* background-color: aqua; */
  list-style: none;
  border-right: 1px dotted var(--vt-c-indigo);
  padding: 0;
}

li {
  /* background-color: aqua; */
  display: flex;

  place-items: center;
  place-content: center;
  width: 100px;
  height: 100px;
  /* font-weight: 100; */

  margin: 10px;
}

li.active {
  border-top: 1px solid var(--vt-c-indigo)
}

.iconify {
  width: 50px;
  height: 50px;
  color: var(--vt-c-indigo);
  /* font-weight: 100; */
  stroke-width: 1;
}

/* header {
  line-height: 1.5;
  max-height: 100vh;
} */

/* .logo {
  display: block;
  margin: 0 auto 2rem;
} */

/* nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
} */

/* nav a.router-link-exact-active {
  color: var(--color-text);
} */

/* nav a.router-link-exact-active:hover {
  background-color: transparent;
} */

/* nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
} */

/* nav a:first-of-type {
  border: 0;
} */

/* @media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
</style>
