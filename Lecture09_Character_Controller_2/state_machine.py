from event_to_string import event_to_string

class StateMachine:
    def __init__(self, start_state, rules):
        self.cur_state = start_state
        self.rules = rules
        self.cur_state.enter(('START', None))
        pass

    def update(self):
        self.cur_state.do()

    def handle_state_event(self, state_event):
        for check_event in self.rules[self.cur_state].keys():
            if check_event(state_event): # 만약 TRUE라면?
                self.cur_state.exit(state_event)
                self.next_state = self.rules[self.cur_state][check_event]
                self.next_state.enter(state_event)
                # 현재 상태가 어떤 이벤트에 의해서 다음상태로 바뀌는지 정보를 표시
                print(f'{self.cur_state.__class__.__name__} ========{event_to_string(state_event)}=========> {self.next_state.__class__.__name__}')
                self.cur_state = self.next_state
                return

        print(f'처리되지 않은 이벤트 {event_to_string(state_event)}가 있습니다.')

    def draw(self):
        self.cur_state.draw()