<template>
  <q-layout view="hHh lpR fFf" class="bg-primary">
    <q-drawer
      class="column justify-between items-center q-pa-xl"
      dark
      :model-value="true"
      :width="500"
      :persistent="true"
      behavior="desktop"
      :show-if-above="true"
    >
      <router-link class="row q-gutter-md items-end" :to="{ name: 'index' }">
        <div>
          <img src="~assets/logo3-56x56.png" />
        </div>
        <div>
          <div class="text-h3">Barberium</div>
          <div>Все для барбершопов и парикмахерских</div>
        </div>
      </router-link>

      <div class="full-width q-gutter-md">
        <div class="text-h3 text-weight-bolder">Sign In</div>
        <q-input outlined v-model="form.login" placeholder="Login" dark />
        <q-input outlined v-model="form.password" placeholder="Password" dark />
        <div>
          <q-btn color="primary" label="Sign In" />
        </div>
      </div>

      <div></div>
    </q-drawer>

    <q-page-container class="Qbg-primary">
      <lavaLamp />

      <div
        class="text-white window-height row justify-center items-center"
        style="position: absolute; z-index: 100"
        v-if="showAbout"
      >
        <IconLogo class="col-3" />

        <div class="column col-6">
          <p class="text-h5">
            Готовые решения для салонов красоты, студий и барбершопов.
          </p>

          <dl>
            <dt>HairMagic</dt>
            <dd>
              Превратите обычную прогулку в приключение! Привлекайте клиентов,
              пока они просто проходят мимо.
            </dd>

            <dt>NeuroTune</dt>
            <dd>Включите AI-радио: музыка, которая чувствует vibe!</dd>

            <dt>Виртуальный Стилист</dt>
            <dd>
              Рискните без риска! Примеряйте новые образы прямо на экране перед
              стрижкой.
            </dd>

            <dt>Salon Assistant</dt>
            <dd>
              Ваш цифровой помощник. Управляйте расписанием, запасами и
              клиентской базой одним касанием.
            </dd>
          </dl>
        </div>
      </div>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { ref } from "vue";
import lavaLamp from "../components/lava-lamp.vue";
import IconLogo from "src/components/icons/IconLogo.vue";
import { Screen } from "quasar";
import { computed } from "vue";

const form = ref({
  login: "",
  password: "",
});

const showAbout = computed(() => {
  return ["lg", "md", "xl"].includes(Screen.name);
});
</script>

<style lang="scss" scoped>
dt {
  font-weight: 600;
  margin-top: 10px;
}
</style>
