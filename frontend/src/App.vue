<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="w-full m-auto flex flex-col items-center">
    <!-- <nav class="w-[85%] mt-2 rounded-lg py-4 bg-gradient-to-r from-blue-500 to-purple-600 shadow-md">
      <div class="container mx-auto flex px-5 justify-between items-center">
        <div class="text-white text-lg font-bold">Your Logo</div>
        <div class="flex space-x-8">
          <RouterLink to="/" class="text-white hover:text-gray-200 font-semibold transition duration-300">Home</RouterLink>
          <RouterLink to="/about" class="text-white hover:text-gray-200 font-semibold transition duration-300">About</RouterLink>
        </div>
      </div>
    </nav> -->
    <div class="container mx-auto mt-8">
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
