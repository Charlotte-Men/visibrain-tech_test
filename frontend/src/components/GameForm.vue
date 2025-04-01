<template>
  <p>Enter a game name to see last Twitch videos about it:</p>
  <div>
    <input 
      v-model="gameName" 
      @keyup.enter="searchVideos" 
      placeholder="Game name"
    />
    <button @click="searchVideos">Search</button>
  </div>
</template>

<script>
  import { ref } from "vue";

  export default {
    emits: ["videos-found"],
    setup(_, { emit }) {
      const gameName = ref("");

      const searchVideos = async () => {
        if (gameName.value.trim()) {
          emit("videos-found", gameName.value.trim());
        }
      };

      return { gameName, searchVideos };
    },
  };
</script>
