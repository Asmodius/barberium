<template>
<div class="sidebar" ref="sidebar">
  <!-- width="280pt" height="254pt" -->
  <div class="fly-menu" @click="ToggleMenu">
    <svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="44px" viewBox="0 0 280.000000 254.000000" preserveAspectRatio="xMidYMid meet">
      <g transform="translate(0.000000,254.000000) scale(0.100000,-0.100000)" fill="#000000" stroke="none">
        <path d="M1840 2450 c-396 -22 -901 -140 -1165 -272 -123 -62 -289 -181 -387 -278 -79 -77 -104 -109 -129 -165 -29 -64 -31 -79 -30 -163 1 -55 7 -107 15 -127 38 -90 137 -173 247 -206 68 -21 135 -23 133 -4 -1 6 -50 31 -109 57 -161 70 -190 105 -183 218 12 209 228 400 638 563 435 173 1155 282 1458 222 154 -31 240 -99 250 -195 9 -93 -70 -213 -194 -295 -198 -132 -527 -255 -725 -271 -60 -5 -90 -14 -128 -36 -104 -59 -81 -109 139 -311 85 -79 187 -181 227 -227 200 -231 217 -471 45 -639 -110 -107 -265 -168 -458 -178 -169 -9 -252 16 -337 103 -46 46 -87 130 -87 177 0 35 -19 95 -36 112 -9 8 -30 15 -49 15 -29 0 -41 -9 -96 -73 -94 -109 -144 -138 -177 -105 -18 18 -14 81 8 142 35 92 222 462 325 641 179 314 317 510 450 640 98 97 167 137 236 138 40 1 49 4 49 18 0 53 -114 119 -206 119 -158 0 -444 -288 -444 -447 0 -58 -19 -100 -181 -398 -197 -366 -356 -707 -387 -835 -23 -96 -24 -118 -3 -139 22 -22 121 -46 151 -36 34 11 81 57 141 137 31 42 60 74 63 71 3 -4 6 -18 6 -33 0 -40 56 -144 96 -179 83 -74 188 -109 344 -118 283 -15 545 73 711 237 204 203 256 444 140 646 -40 68 -168 203 -261 274 -42 32 -129 92 -193 135 -65 43 -117 79 -115 80 2 2 64 10 138 20 365 46 682 178 814 340 91 112 116 256 65 365 -95 203 -350 285 -809 260z"/>
      </g>
    </svg>
  </div>

  <div class="main-menu" :class="`${is_expanded && 'is-expanded'}`">
    <div class="menu-item"><RouterLink :to="{name: 'setup'}"><IconSetup /></RouterLink></div>
    <div class="menu-item"><RouterLink :to="{name: 'show'}"><IconSmilePlus /></RouterLink></div>
    <div class="menu-item"><RouterLink :to="{name: 'week'}"><IconEvent /></RouterLink></div>
    <div class="menu-item"><RouterLink :to="{name: 'look'}"><IconArOnYou /></RouterLink></div>
    <div class="menu-item"><RouterLink :to="{name: 'musik'}"><IconMusic /></RouterLink></div>
  </div>
</div>
</template>

<script setup>
import { RouterLink, useRoute } from 'vue-router'
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'

import IconSetup from './icons/IconSetup.vue'
import IconSmilePlus from './icons/IconSmilePlus.vue'
import IconArOnYou from './icons/IconArOnYou.vue'
import IconEvent from './icons/IconEvent.vue'
import IconMusic from './icons/IconMusic.vue'

const is_expanded = ref(false)
const route = useRoute()
const sidebar = ref(null)

const ToggleMenu = () => {
  is_expanded.value = !is_expanded.value
}

watch(route, () => {
  is_expanded.value = false;
})

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
});

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside);
})

const handleClickOutside = (event) => {
  if (sidebar.value && !sidebar.value.contains(event.target)) {
    is_expanded.value = false;
  }
}
</script>

<style lang="scss" scoped>
.sidebar {
  margin: 10px;
  border: 1px solid #32a1ce;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  width: 60px;
  position: absolute;
}

.fly-menu {
  width: 50px;
  height: 50px;
  padding: 0;
  cursor: pointer;
  padding: 5px;
}

.main-menu {
  padding: 5px;
  opacity: 0;
  max-height: 0;
  overflow: hidden;
  transform: scaleY(0);
  transition: transform 400ms ease 0ms;

  &.is-expanded {
    transform: scaleY(1);
    transition: transform 400ms ease 0ms;
    opacity: 1;
    max-height: 100%;
  }
}

.iconify {
  width: 46px;
  height: 46px;
  /* color: red; */
  /* color: var(--vt-c-indigo); */
  /* stroke-width: 1; */
}

</style>
