<template>
  <q-layout>
    <q-header elevated class="text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title><h4>Barberium</h4></q-toolbar-title>
      </q-toolbar>
      <q-tabs>
        <q-route-tab to="#home" label="Home" />
        <q-route-tab to="#hair-magic" label="HairMagic" />
        <q-route-tab to="#salon-assistant" label="Salon Assistant" />
        <q-route-tab to="#glamour-stock" label="Glamour Stock" />
        <q-route-tab to="#neuro-tune" label="NeuroTune" />
      </q-tabs>
    </q-header>

    <!-- <q-page-container> -->
      <q-carousel class="text-white" v-model="slide" animated arrows navigation infinite>
        <q-carousel-slide :name="1" img-src="https://cdn.quasar.dev/img/mountains.jpg">
          <h2>Откройте для себя HairMagic<br></h2>
          <p>HairMagic - эта программа превратит каждую прогулку мимо вашего салона в увлекательное приключение!</p>
        </q-carousel-slide>
        <q-carousel-slide :name="2" img-src="https://cdn.quasar.dev/img/parallax1.jpg" />
        <q-carousel-slide :name="3" img-src="https://cdn.quasar.dev/img/parallax2.jpg" />
        <q-carousel-slide :name="4" img-src="https://cdn.quasar.dev/img/quasar.jpg" />

        <!-- <q-carousel-slide name="style" class="column no-wrap flex-center">
          <q-icon name="style" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="tv" class="column no-wrap flex-center">
          <q-icon name="live_tv" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="layers" class="column no-wrap flex-center">
          <q-icon name="layers" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem }}
          </div>
        </q-carousel-slide>
        <q-carousel-slide name="map" class="column no-wrap flex-center">
          <q-icon name="terrain" size="56px" />
          <div class="q-mt-md text-center">
            {{ lorem }}
          </div>
        </q-carousel-slide> -->
      </q-carousel>

    <!-- </q-page-container> -->

  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// const lorem = 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.'
const slide = ref(1)
</script>

<style>
  .q-header {
    background-color: rgba(0, 0, 0, 0);
  }
</style>
