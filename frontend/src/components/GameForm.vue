<template>
  <form onsubmit="return false">
    <p>Enter a game name to see last Twitch videos about it:</p>
    <div>
      <input 
        v-model="gameName" 
        @keyup.enter="searchVideos" 
        placeholder="Game name"
      />
      <button @click="searchVideos">Search</button>
    </div>
  </form>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const gameName = ref("");

    function searchVideos() {
      if (gameName.value.trim()) {
        console.log(gameName.value)
      }
    };

    return { gameName, searchVideos };
  },
};
</script>
