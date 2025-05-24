<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="w-full m-auto flex flex-col items-center">
    <div class="container mx-auto">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
nav a.router-link-exact-active {
  border-bottom: 2px solid #fff;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

@media (min-width: 1024px) {
  nav {
    text-align: center;
  }
}
</style>
