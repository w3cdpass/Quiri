<script lang="ts">
	let { float = 'right' }: { float: 'left' | 'right' } = $props();

	let openDialog = $state(false);

	function toggle() {
		openDialog = !openDialog;
	}
</script>

<button
	onclick={toggle}
	class="fixed bottom-5 flex h-5 w-5 cursor-pointer items-center justify-center rounded-full bg-gray-300 p-7"
	class:right-5={float === 'right'}
	class:left-5={float === 'left'}
>
	{openDialog ? 'close' : 'open'}
</button>

{#if openDialog}
	<div 
		class="fixed bottom-20"
		class:right-5={float === 'right'}
		class:left-5={float === 'left'}
	>
		<div class="bg-white rounded-lg shadow-lg  p-4">
			<!-- Welcome & opening message -->
			<div class="mb-3">
				<h2 class="text-lg font-semibold text-gray-800">Welcome!</h2>
				<p class="text-sm text-gray-600">
					Hi there 👋, how can I help you today?
				</p>
			</div>

			<form
				onsubmit={(e) => {
					e.preventDefault();
				}}
				class="flex items-center gap-2"
			>
				<input
					type="text"
					placeholder="Type your message..."
					class="flex-1 rounded-lg border border-gray-300 px-3 py-2 text-sm outline-none focus:border-green-400 focus:ring-1 focus:ring-green-300"
				/>
				<button
					type="submit"
					class="rounded-lg bg-green-500 px-4 py-2 text-sm font-medium text-white hover:bg-green-600 active:bg-green-700 transition-colors"
				>
					Send
				</button>
			</form>
		</div>
	</div>
{/if}
