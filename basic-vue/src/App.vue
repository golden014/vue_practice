<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import { reactive } from 'vue';

const state = reactive({
  likes: 0
});

const addLike = () => {
  if (state.likes < 10) {
    state.likes++
  } else {
    alert("cant go any further")
  }
}
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper" @click="addLike" >
      <!-- <button @click="state.likes++"></button> -->
      <p>{{ state.likes }}</p>
      <HelloWorld :msg= "state.likes.toString()"/>
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>



<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
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
}
</style>
